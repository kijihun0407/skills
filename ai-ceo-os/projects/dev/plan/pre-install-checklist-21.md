# ✅ 사전 설치 체크리스트 21개 (과제 C-08.5)

> **마감**: 5-1 D-1 (5-1 라이브 전날 23:59)
> **제출**: Supabase / GitHub / DESIGN.md 적용 **스크린샷 3장**
> **지원**: 디스코드 `#install-help` + 스쿼드 상호 지원 + dev-team FAQ 10개
> **클리닉**: 미완료자 → 5-1 당일 09:30 별도 설치 클리닉 세션

---

## 🎯 왜 이걸 지금 해야 하나

**대표님 설명**:
> "여러분이 5-1에서 AI 붙이려면, 오늘 안 본 것들 10개를 설치해야 돼요.
> 설치하면서 막히면 5-1 라이브 30분 날아가요. 그럼 핵심 강의 못 들어요.
>
> 그래서 오늘 여러분에게 '설치 체크리스트 21개'를 드립니다.
> **dev-team이 D-5에 먼저 다 해봤고, 막힌 포인트 10개 FAQ로 정리해놨어요.**"

**dropout-patterns.md 근거**: 1주차 이탈 1번 원인 = "설치/셋업 어려움"

---

## ☁️ Part 1. 계정 + API (9개)

- [ ] **1. Supabase 프로젝트 생성** — [supabase.com](https://supabase.com) 이메일 가입 → New Project → DB 비밀번호 안전 저장 (패스워드 매니저)
- [ ] **2. Claude API 키 발급** — [console.anthropic.com](https://console.anthropic.com) → **본인 카드** 등록 → API key 발급
- [ ] **3. GitHub Private Repo 생성** — [github.com/new](https://github.com/new) → **Private** 체크 → bootcamp-kit 파일 업로드
- [ ] **4. Vercel CLI 설치 + GitHub 연결** — `npm i -g vercel` → `vercel login` → GitHub 계정 연결
- [ ] **5. Sentry 프로젝트 생성** — [sentry.io](https://sentry.io) 가입 → Next.js 프로젝트 생성 → DSN 복사
- [ ] **6. 토스페이먼츠 테스트 계정** — [developers.tosspayments.com](https://developers.tosspayments.com) → 테스트 클라이언트 키 + 시크릿 키 발급
- [ ] **7. Discord `#install-help` 가입** — 초대 링크 (운영진 배포) → 자기소개 1줄
- [ ] **8. `claude-md-templates` 레포 클론** — `git clone https://github.com/abhishekray07/claude-md-templates.git`
- [ ] **9. `next-supabase-stripe-starter` 사전 클론** — `git clone https://github.com/KolbySisk/next-supabase-stripe-starter.git`

---

## 🎨 Part 2. DESIGN.md 선택 (3개)

- [ ] **10. VoltAgent/awesome-design-md 레포 훑기** — [github.com/VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) → 66+ 브랜드 스캔
- [ ] **11. 프로젝트 취향 맞는 1개 선택** — Stripe / Linear / Vercel / Supabase / Apple / Notion 중 하나
- [ ] **12. 프로젝트 루트에 `DESIGN.md`로 저장** — 반드시 **파일명 `DESIGN.md`** (대문자 유지)

---

## 📦 Part 3. bootcamp-kit 적용 (6개)

- [ ] **13. `PLAN.md` 채워넣기** — 4-2 라이브에서 이미 완성. 내 프로젝트 루트에 복사.
- [ ] **14. `INTERVIEW.md` 자가 인터뷰 10답변** — 4-2 PART C+ 인터뷰 셋업으로 완료.
- [ ] **15. `HABITS.md` 자가 체크 (5개+)** — 오늘 써본 습관 5개 이상 체크.
- [ ] **16. `DESIGN.md` 프로젝트 적용** — Step 10~12와 연계. `README.md` 하단에 "디자인: Linear 스타일" 명시.
- [ ] **17. `배포공식카드.md` 숙지** — 10분 공식 4단계 암기.
- [ ] **18. `CLAUDE.md` 규칙 복사** — 내 프로젝트 루트에 `CLAUDE.md` 저장. Claude Code가 자동 인식.

---

## 🛠 Part 4. 로컬 환경 (3개)

- [ ] **19. VSCode + Claude Code 설치 확인** — `claude --version` 실행해서 버전 출력 확인
- [ ] **20. `.env` 파일 생성 + Supabase 1개 토큰 테스트** — `.env.local`에 `NEXT_PUBLIC_SUPABASE_URL` 넣기. `.gitignore`에 `.env*` 확인.
- [ ] **21. `localhost:3000` 정상 작동** — `npm run dev` → 브라우저 `localhost:3000` → 기본 화면 보이는지

---

## 📸 제출물 (5-1 D-1 23:59까지)

### 스크린샷 3장

1. **Supabase 프로젝트 대시보드** (프로젝트 이름 보이게)
2. **GitHub Private Repo** (Repo 이름 + Private 뱃지 보이게)
3. **DESIGN.md 프로젝트에 복사된 화면** (VSCode 파일 트리 + DESIGN.md 내용 일부)

### 제출 방법

- 디스코드 `#submissions` 채널
- 형식: `[기수-닉네임] 사전설치 완료 + 스크린샷 3장`

---

## 🆘 막혔을 때

### Step 1: FAQ 먼저
`faq/01~10.md` 참조 — dev-team이 D-5에 먼저 해본 결과

### Step 2: 디스코드
`#install-help` 채널에 에러 메시지 **전체 복사 + 스크린샷**

### Step 3: 스쿼드 리더
같은 스쿼드 리더에게 DM — 24시간 내 답변 약속

### Step 4: 설치 클리닉
**5-1 당일 09:30** (라이브 30분 전 별도 세션) — 모든 미완료자 참석.

---

## ⏱ 예상 소요 시간

- Part 1 계정 + API: **60분** (각 7분 × 9개)
- Part 2 DESIGN.md 선택: **15분**
- Part 3 bootcamp-kit 적용: **20분**
- Part 4 로컬 환경: **30분**
- **총: 약 2시간** (중간 휴식 포함)

**분할 권장**: D+1 Part 1 → D+2 Part 2,3 → D+3 Part 4 → D+4~6 여유분

---

## 🎁 완료 후 보상

- 5-1 라이브 **전 설치 완료자**: 라이브 중 스쿼드 리더 후보 추천
- 스크린샷 제출률 100% 달성 스쿼드: **스쿼드 전체 특별 혜택** (CPO 추가 공지)

---

**대표님 마무리 멘트**:

> "오늘 첫 랜딩 만들었고, 다음 주 준비까지 끝났어요.
> 5-1 라이브에서는 **설치 다 된 상태에서 AI 기능 붙이는 것만** 집중합니다.
> 그게 **제대로 가르치는 방법**이에요."
