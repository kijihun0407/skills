#!/usr/bin/env python3
"""
instagram_apify_fetch.py — Apify 기반 인스타그램 데이터 수집

목적:
  로그인 없이 내 계정 + 경쟁 계정 포스트/프로필 데이터를 수집.
  Meta Graph API 토큰 없이도 동작 (Apify가 대신 처리).

필요 환경변수 (.env):
  APIFY_TOKEN=apify_api_...

사용법:
  python execution/instagram_apify_fetch.py
  python execution/instagram_apify_fetch.py --mode profile   # 프로필 요약만
  python execution/instagram_apify_fetch.py --mode posts     # 최근 포스트만
  python execution/instagram_apify_fetch.py --mode all       # 전부 (기본값)

출력:
  knowledge/channel-data/apify_YYYYMMDD.json
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import requests
except ImportError:
    print("[오류] pip install requests", file=sys.stderr)
    sys.exit(1)

# ─────────────────────────────────────────
# 설정
# ─────────────────────────────────────────

MY_ACCOUNT = "ai.saver_"

COMPETITOR_ACCOUNTS = [
    "biggie_ai",       # 핵심 벤치마크 — 트렌드 중심
    "ai_dori_",        # 핵심 벤치마크 — 활용법 중심
    "ai_ing_",         # 핵심 벤치마크 — 정보 중심
    "brivvy_ai",       # 비노출형
    "ai.trend.kr",     # AI 트렌드
    "ai_freaks.kr",    # AI 프릭스
    "ai.favmag",       # AI 패브매거진
    "promppy_com",     # 프롬프트 전문
    "ai.yeongseon",    # AI 크리에이터 (bywaviboy 대체 — 180K 초과 제외)
    "thisiskeepkwan",  # AI 콘텐츠 크리에이터
]

ALL_ACCOUNTS = [MY_ACCOUNT] + COMPETITOR_ACCOUNTS

APIFY_BASE = "https://api.apify.com/v2"
ACTOR_ID = "apify~instagram-scraper"  # 공식 Instagram Scraper

POSTS_PER_ACCOUNT = 20  # 계정당 최근 포스트 수
POLL_INTERVAL = 5       # 상태 확인 간격 (초)
TIMEOUT = 300           # 최대 대기 시간 (초)


# ─────────────────────────────────────────
# 유틸
# ─────────────────────────────────────────

def load_token() -> str:
    token = os.getenv("APIFY_TOKEN")
    if not token:
        env_file = Path(".env")
        if env_file.exists():
            for line in env_file.read_text(encoding="utf-8").splitlines():
                if line.startswith("APIFY_TOKEN="):
                    token = line.split("=", 1)[1].strip()
                    break
    if not token:
        print("[오류] APIFY_TOKEN 환경변수를 설정하세요.", file=sys.stderr)
        sys.exit(1)
    return token


def run_actor(token: str, input_data: dict) -> str:
    """Actor를 실행하고 run_id를 반환."""
    url = f"{APIFY_BASE}/acts/{ACTOR_ID}/runs"
    resp = requests.post(
        url,
        params={"token": token},
        json=input_data,
        timeout=30,
    )
    if resp.status_code not in (200, 201):
        print(f"[오류] Actor 실행 실패 ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)
    run_id = resp.json()["data"]["id"]
    print(f"[실행] Actor 시작 — run_id: {run_id}")
    return run_id


def wait_for_run(token: str, run_id: str) -> bool:
    """Actor 실행 완료까지 대기. 성공 여부 반환."""
    url = f"{APIFY_BASE}/actor-runs/{run_id}"
    elapsed = 0
    while elapsed < TIMEOUT:
        resp = requests.get(url, params={"token": token}, timeout=30)
        status = resp.json()["data"]["status"]
        print(f"[대기] {elapsed}s — 상태: {status}")
        if status == "SUCCEEDED":
            return True
        if status in ("FAILED", "ABORTED", "TIMED-OUT"):
            print(f"[오류] Actor 실패: {status}", file=sys.stderr)
            return False
        time.sleep(POLL_INTERVAL)
        elapsed += POLL_INTERVAL
    print("[오류] 타임아웃", file=sys.stderr)
    return False


def fetch_dataset(token: str, run_id: str) -> list[dict]:
    """Actor 실행 결과 데이터셋 반환."""
    url = f"{APIFY_BASE}/actor-runs/{run_id}/dataset/items"
    resp = requests.get(
        url,
        params={"token": token, "format": "json", "clean": "true"},
        timeout=60,
    )
    if resp.status_code != 200:
        print(f"[경고] 데이터셋 조회 실패 ({resp.status_code})", file=sys.stderr)
        return []
    return resp.json()


# ─────────────────────────────────────────
# 메인 로직
# ─────────────────────────────────────────

def collect_profile_and_posts(token: str, accounts: list[str]) -> list[dict]:
    """
    apify/instagram-scraper 로 프로필 + 최근 포스트 수집.
    """
    input_data = {
        "directUrls": [f"https://www.instagram.com/{a}/" for a in accounts],
        "resultsType": "posts",
        "resultsLimit": POSTS_PER_ACCOUNT,
        "addParentData": True,  # 프로필 정보도 포함
        "scrapePostsUntilDate": None,
    }

    run_id = run_actor(token, input_data)
    success = wait_for_run(token, run_id)
    if not success:
        return []
    return fetch_dataset(token, run_id)


def _username_from_url(url: str) -> str:
    """https://www.instagram.com/ai.saver_/ → ai.saver_"""
    url = url.rstrip("/")
    if "instagram.com/" in url:
        return url.split("instagram.com/")[-1].split("/")[0]
    return ""


def summarize(items: list[dict]) -> dict:
    """
    수집 데이터를 계정별로 집계.
    출력:
      {username: {followers, posts_count, avg_likes, avg_comments, top_posts}}
    """
    from collections import defaultdict

    accounts: dict[str, dict] = {}

    for item in items:
        username = (
            item.get("ownerUsername")
            or item.get("username")
            or _username_from_url(item.get("url") or "")
            or "unknown"
        )

        if username not in accounts:
            accounts[username] = {
                "username": username,
                "followers": item.get("ownerFollowersCount") or item.get("followersCount"),
                "following": item.get("ownerFollowingCount") or item.get("followingCount"),
                "biography": item.get("ownerBiography") or item.get("biography"),
                "posts": [],
            }

        # 포스트 정보
        post = {
            "id": item.get("id"),
            "type": item.get("type"),                  # Image / Video / Sidecar
            "timestamp": item.get("timestamp"),
            "caption": (item.get("caption") or "")[:100],
            "likes": item.get("likesCount") or 0,
            "comments": item.get("commentsCount") or 0,
            "video_plays": item.get("videoViewCount") or 0,
            "url": item.get("url"),
        }
        accounts[username]["posts"].append(post)

    # 집계
    summary = {}
    for uname, data in accounts.items():
        posts = data["posts"]
        if not posts:
            continue

        likes_list = [p["likes"] for p in posts]
        comments_list = [p["comments"] for p in posts]
        plays_list = [p["video_plays"] for p in posts if p["video_plays"]]

        top_posts = sorted(posts, key=lambda x: x["likes"] + x["video_plays"], reverse=True)[:5]

        summary[uname] = {
            "username": uname,
            "followers": data["followers"],
            "following": data["following"],
            "biography": data["biography"],
            "posts_scraped": len(posts),
            "avg_likes": round(sum(likes_list) / len(likes_list), 1) if likes_list else 0,
            "avg_comments": round(sum(comments_list) / len(comments_list), 1) if comments_list else 0,
            "avg_video_plays": round(sum(plays_list) / len(plays_list), 1) if plays_list else 0,
            "top_posts": top_posts,
        }

    return summary


def save_output(data: dict) -> Path:
    out_dir = Path("knowledge/channel-data")
    out_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y%m%d")
    out_path = out_dir / f"apify_{date_str}.json"
    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


def print_summary(summary: dict) -> None:
    print("\n" + "=" * 60)
    print(f"{'계정':<20} {'팔로워':>8} {'평균좋아요':>10} {'평균조회수':>10}")
    print("-" * 60)

    my = summary.get(MY_ACCOUNT)
    if my:
        print(f"★ {my['username']:<18} {str(my['followers'] or '-'):>8} "
              f"{my['avg_likes']:>10} {my['avg_video_plays']:>10}")
        print("-" * 60)

    for uname, data in summary.items():
        if uname == MY_ACCOUNT:
            continue
        print(f"  {data['username']:<18} {str(data['followers'] or '-'):>8} "
              f"{data['avg_likes']:>10} {data['avg_video_plays']:>10}")

    print("=" * 60)


def main() -> None:
    mode = "all"
    if "--mode" in sys.argv:
        idx = sys.argv.index("--mode")
        mode = sys.argv[idx + 1]

    token = load_token()

    print(f"[시작] 수집 대상: 내 계정 1개 + 경쟁 계정 {len(COMPETITOR_ACCOUNTS)}개")
    print(f"[계정] {', '.join(ALL_ACCOUNTS)}")

    items = collect_profile_and_posts(token, ALL_ACCOUNTS)

    if not items:
        print("[경고] 수집된 데이터 없음", file=sys.stderr)
        sys.exit(1)

    summary = summarize(items)

    output = {
        "fetched_at": datetime.now().isoformat(),
        "my_account": MY_ACCOUNT,
        "competitor_accounts": COMPETITOR_ACCOUNTS,
        "raw_item_count": len(items),
        "summary": summary,
    }

    out_path = save_output(output)
    print_summary(summary)
    print(f"\n[완료] {out_path} 저장 ({len(items)}건 원본 데이터)")
    print("[참고] 이 파일의 숫자만 인용할 것. 추정 금지 (Zero-Inference)")


if __name__ == "__main__":
    main()
