# 기술 스택 + 웹 핵심 개념

> 에이나우 고정 스택 6개로 100% 가능.
> 선택지 10개 비교 X, 검증된 6개만 쓴다.

---

## 에이나우 고정 스택 6개

| # | 스택 | 역할 | 왜 이것인가 |
|:---|:---|:---|:---|
| 1 | **Next.js** | 웹사이트 기본 프레임워크 | 프론트+백엔드 한 번에 + Vercel 무료 배포 |
| 2 | **Tailwind** | 디자인 (스타일링) | 말로 디자인 가능한 CSS |
| 3 | **Supabase** | DB + 인증 + Storage | 올인원 무료 (PostgreSQL+Auth+Storage) |
| 4 | **Claude API** | AI 기능 (챗봇/요약/추천) | 가장 똑똑한 AI, 긴 맥락 200K 토큰 |
| 5 | **Vercel** | 배포 (호스팅) | git push = 자동 배포, 무료, HTTPS 자동 |
| 6 | **토스페이먼츠** | 결제 (신용카드/계좌) | 한국 결제 공식, 문서 최고 |

### 각 스택 실전 팁

**Next.js**
- React+Express 분리보다 3배 빠름
- 경험담: React+Express로 한 기능 3일 → Next.js로 3시간

**Tailwind**
- `<div className="bg-gray-900 text-white p-8">` = 다크 카드 한 줄

**Supabase**
- PostgreSQL DB + 인증(카카오/구글/이메일) + Storage 세 가지를 하나로
- RLS (Row Level Security): 반드시 활성화. 비활성화 시 해커 천국

**Claude API 비용 방어선 3개**
1. `max_tokens: 500` 고정
2. 입력 1000자 cap
3. IP당 일 10회 Rate Limit
→ 이거 안 하면 월 수백 달러 청구 가능

**Vercel**
- AWS EC2 대신 쓰면 초보자 지옥 탈출
- git push → Vercel이 자동으로 빌드 + 배포 + HTTPS

---

## 웹 핵심 개념 6개 (AI한테 시킬 때 알아야 할 만큼만)

### 개념 1: HTTP / HTTPS
- 쉽게: 웹 데이터 오가는 약속
- 비유: 편지 주고받을 때 우표+주소 약속
- HTTPS = HTTP + 자물쇠 🔒 (보안). 로그인·결제 필수
- AI한테: "이 API는 **HTTPS로만** 요청 가능하게"

### 개념 2: 도메인 / DNS
- 쉽게: 주소를 IP로 바꿔주는 전화번호부
- 비유: "강남역 1번 출구"로 찾지 좌표(142.250.x.x)로 안 찾잖아요
- AI한테: "vercel 도메인을 mydomain.com으로 연결"

### 개념 3: Client / Server
- 쉽게: 손님(Client) / 가게(Server)
- 비유: 식당에서 손님이 주문 → 주방이 만들어줌
- **중요 보안 규칙**: API 키, 카드 키 = 무조건 서버에서만
- Next.js: `NEXT_PUBLIC_` 접두사는 클라이언트에 노출 → 민감한 건 절대 쓰지 말 것

### 개념 4: Request / Response
- 쉽게: 주문 / 답변
- 상태 코드: **200** OK / **404** 없음 / **500** 서버 에러 / **401** 로그인 필요
- ⚠️ HTTP 200 ≠ 정상: 빈 fallback 페이지도 200 반환 가능. 실제로 열어봐야 함

### 개념 5: REST API
- 쉽게: 가게 주문서 표준
- 4가지 동작 (CRUD):
  - **GET**: 조회(Read)
  - **POST**: 생성(Create)
  - **PUT**: 수정(Update)
  - **DELETE**: 삭제(Delete)

### 개념 6: JSON
- 쉽게: AI와 나누는 대화 문법
- 비유: 엑셀 = 행/열, JSON = 중괄호/따옴표
- 예시: `{"name": "홍길동", "age": 30}`

---

## 사전 설치 9개

| # | 항목 | 핵심 주의사항 |
|:---|:---|:---|
| 1 | **Supabase** 프로젝트 | RLS 반드시 활성화 |
| 2 | **Claude API** 키 | 본인 카드, Git 커밋 금지 |
| 3 | **GitHub** Private Repo | 반드시 Private! |
| 4 | **Vercel** CLI + GitHub 연결 | npm i -g vercel |
| 5 | **Sentry** | Next.js 선택, DSN 복사 |
| 6 | **토스페이먼츠** 테스트 | 테스트 클라이언트+시크릿 키 |
| 7 | **Discord** #install-help | 자기소개 1줄 |
| 8 | **claude-md-templates** 클론 | GitHub 레포 클론 |
| 9 | **next-supabase-stripe-starter** 클론 | GitHub 레포 클론 |

### .env.local 기본 구조
```bash
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...
ANTHROPIC_API_KEY=sk-ant-...
TOSS_SECRET_KEY=sk_test_...

# .gitignore에 반드시:
.env
.env.local
.env.*.local
```

---

## DESIGN.md — awesome-design-md

레포: `github.com/VoltAgent/awesome-design-md` (66+ 브랜드)

**CEO 추천 TOP 5**

| 브랜드 | 특징 | 어울리는 프로젝트 |
|:---|:---|:---|
| **Linear** | 생산성 도구 미니멀 | 업무 도구, SaaS MVP |
| **Vercel** | 개발자 친화 다크 | 기술 제품 |
| **Stripe** | 결제 서비스 깔끔 | 금융, 상거래 |
| **Supabase** | 오픈소스 감성 | 커뮤니티, 플랫폼 |
| **Notion** | 문서 도구 친근 | 개인 생산성, 교육 |

⚠️ 파일명 주의: `DESIGN.md` (대문자 필수. 소문자면 Claude가 못 찾음)
