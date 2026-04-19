# 프로젝트 아키텍처 — 본사 ↔ 사업부 구조

> Claude Code는 "지금 열려 있는 폴더"를 기준으로 맥락을 잡는다.
> 어느 사업부 폴더에 cd 하느냐가 곧 "누구를 호출하느냐"다.

---

## 전체 구조도

```
ai-ceo-os/                         ← 본사
├── CLAUDE.md                      ← 전사 헌법 (회사 전체 미션)
├── agents/                        ← C-Suite 9명 (전사 임원 원본)
├── skills/                        ← 공통 스킬
├── context/                       ← 회사 DNA
├── knowledge/                     ← 지식베이스
├── directives/                    ← 본사 SOP
├── execution/                     ← Python 스크립트 (Layer 3)
│
└── projects/                      ← 사업부들
    ├── marketing/                 ← 마케팅 사업부
    │   ├── CLAUDE.md
    │   ├── agents/ (CCO, CMO)
    │   ├── skills/
    │   ├── context/
    │   ├── rules/
    │   └── directives/
    ├── dev/                       ← 개발 사업부
    ├── operations/                ← 운영 사업부
    └── customer/                  ← 고객 사업부
```

---

## 클로드코드 4대 활용 영역 (ROI 기준)

| # | 영역 | 무슨 일 | 폴더 | 돈 버는 이유 |
|:---|:---|:---|:---|:---|
| 1 | **마케팅** | 콘텐츠 기획/제작, 광고 분석, 퍼널 | `projects/marketing/` | 매출 직결 |
| 2 | **바이브코딩/개발** | 랜딩페이지, 자동화 스크립트 | `projects/dev/` | 외주 비용 제거 + 속도 10배 |
| 3 | **운영/관리** | 계획, 데이터 정리, CRM | `projects/operations/` | 시간 회수 |
| 4 | **프로젝트 팀 운영** | 사업부 간 조율 | (본사 레벨) | 1인이 팀처럼 일함 |

> ROI 원칙: AI를 쓰는 이유는 시간을 벌거나 비용을 줄이기 위해서다. ROI가 안 나오면 하지 않는다.

---

## 본사 vs 사업부 역할 분담

| 구분 | 본사 (루트) | 사업부 (projects/xxx/) |
|:---|:---|:---|
| **역할** | 전사 헌법 + 공용 자산 | 특정 업무 도메인 실전 작업장 |
| **CLAUDE.md** | 회사 미션/비전/금지/톤 | 이 팀의 목표/담당자/작업 규칙 |
| **에이전트** | C-Suite 9명 (원본) | 전담 1~3명 선택 (@참조) |
| **스킬** | 공통 스킬 | 도메인 특화 스킬 |
| **질문 예시** | "우리 회사 방향이 뭐야?" | "이번 주 광고 예산 배분해줘" |

---

## cd 명령 = 팀 전환

```bash
# 본사 전략 질문
cd ai-ceo-os && claude
"우리 사업 방향이 뭐야?" → C-Suite 전체 관점

# 마케팅 실무
cd projects/marketing && claude
"이번 주 릴스 기획해줘" → CCO+CMO 집중 + 채널 규칙 자동 로드

# 고객 응대
cd projects/customer && claude
"DM 응대 초안 써줘" → CXO 집중 + 응대 룰 자동 로드

# 개발 작업
cd projects/dev && claude
"예약 페이지 수정해줘" → CTO 집중 + 보안 체크 자동 로드
```

---

## 복제 전략 (하나 만들고 복제)

```bash
# 첫 번째 사업부 (30~40분)
mkdir -p projects/marketing/{agents,skills,context,rules,directives}

# 두 번째 사업부 (10분) - Claude에게 시키기
"projects/marketing 구조를 복제해서
 projects/customer 사업부를 만들어줘.
 담당 임원은 CXO로, 미션은 '고객 재구매/이탈 방지'로 바꿔줘."

# 세 번째 이후: 5분
```

---

## 우리 프로젝트 현재 상태

| 사업부 | 담당 임원 | 핵심 스킬 | 상태 |
|:---|:---|:---|:---|
| `marketing/` | CCO, CMO | 릴스 대본, 캐러셀, 업로드 최적화 | ✅ 완성 |
| `dev/` | CTO | 자동화 스크립트, Claude Code 가이드 | ✅ 완성 |
| `operations/` | COO | 주간 브리핑, 수익화 로드맵, 워크플로우 자동화 | ✅ 완성 |
| `customer/` | CXO, CCO | DM 응대, DM 자동화, 커뮤니티, 프로필 링크 | ✅ 완성 |
