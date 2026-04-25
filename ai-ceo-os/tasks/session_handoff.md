# Session Handoff Note

> 세션 종료 시 코뿔소가 작성하는 인수인계 노트입니다.
> 다음 세션 시작 시 이 파일을 가장 먼저 읽어 연속성을 확보합니다.

---

## 최근 세션 요약 (2026-04-25)

### 완료한 것

1. **Apify 인스타그램 스크래퍼 구축**
   - `execution/instagram_apify_fetch.py` — 내 계정 + 경쟁계정 10개 자동 수집
   - 매주 월요일 08:03 시스템 crontab 자동 실행 등록
   - 수집 데이터: `knowledge/channel-data/apify_YYYYMMDD.json`
   - 경쟁계정: biggie_ai, ai_dori_, ai_ing_, brivvy_ai, ai.trend.kr, ai_freaks.kr, ai.favmag, promppy_com, ai.yeongseon, thisiskeepkwan

2. **계정명 @ai.saver_ 확정**
   - 인스타그램 앱에서 직접 확인 후 변경 완료
   - 전체 파일 일괄 업데이트 완료

3. **주간 콘텐츠 자동화 파이프라인 설계 완성**
   - `directives/canva-bulk-create-sop.md` — CSV→Canva 업로드 단계별 가이드
   - `directives/weekly-content-automation.md` — 릴스3+캐러셀2 주간 마스터 SOP

4. **이번 주 캐러셀 2종 대본 + CSV 생성**
   - 캐러셀 1: GPT-5.5 직장인 필수 기능 5가지 (화요일 12:00 발행 예정)
   - 캐러셀 2: ChatGPT vs Claude vs Gemini 직장인 비교 (목요일 19:00 발행 예정)
   - CSV 위치: `.tmp/carousel_20260425_GPT55기능.csv` / `.tmp/carousel_20260425_AI3대툴비교.csv`
   - 산출물: `outputs/2026/04/25/[캐러셀]_이번주_캐러셀2종_대본+CSV.md`

5. **Canva Pro 결제 + 템플릿 세팅 진행 중**
   - 1080×1350px, 7페이지, 배경색 + Pretendard 폰트 설정 완료
   - **미완료**: 대량 제작(Bulk Create) 변수 연결 + 슬라이드 생성

### 현재 상태

- **계정명**: @ai.saver_ (인스타그램)
- **AI 비서 이름**: 코뿔소
- **채널**: 인스타그램 초기 운영 (팔로워 거의 없음)
- **상품**: 전자책 + 프롬프트 기획 단계 (미출시)
- **Canva**: Pro 결제 완료, 템플릿 세팅 중단 상태

### ⚠️ 다음 세션 시작 위치 (여기서 이어서)

**Canva 템플릿 변수 연결 마저 완료하기**

```
현재 상태: Canva에서 대량 제작 클릭 → CSV 업로드까지 완료
다음 단계: 각 페이지 텍스트 박스에 변수 연결
```

1. Canva 열기 → 어제 만든 캐러셀 템플릿 열기
2. 상단 앱 → 대량 제작 → CSV 재업로드 (`.tmp/carousel_20260425_GPT55기능.csv`)
3. 1페이지 `slide1_title` 텍스트 박스 클릭 → 변수 연결
4. 2~7페이지 동일하게 연결
5. 생성 → PNG 다운로드
6. 두 번째 CSV(`AI3대툴비교.csv`)도 동일 반복
7. 인스타그램 예약 발행 (화 12:00 / 목 19:00)

### 주의사항

- 에이전트 파일들 (agents/ 하위)의 "김이사" 표기는 유지 — CEO 지시
- 릴스 대본: 반드시 [후킹] → [본문] → [CTA] 3단 구조 + @ai.saver_ 포함
- 인스타 계정 가용성 확인: curl 사용 금지, 반드시 앱에서 직접 확인
- 직장 병행 → 시간 효율 최우선
- 3개월 목표: 팔로워 4만 + 월 수익 100~200만원

---

_마지막 업데이트: 2026-04-25_
