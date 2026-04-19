# SOP: 바이브코딩 실전 가이드

> 바이브코딩 = 내 기획력 × AI 실행력
> PLAN.md → Plan Mode → DCR → git push → 써보며 고침

---

## 작업 시작 전 필수 체크 (CEO 5단계)

| Step | 체크 | 방법 |
|:---:|:---|:---|
| 1 | CLAUDE.md 있는가? | 프로젝트 루트 확인 |
| 2 | PLAN.md 완성되어 있는가? | 11섹션 채워져 있는지 |
| 3 | DESIGN.md 선택했는가? | awesome-design-md에서 선택 |
| 4 | .env.local에 키 있는가? | Supabase URL + Claude API 키 |
| 5 | .gitignore에 .env* 있는가? | 커밋 전 반드시 확인 |

---

## Plan Mode 활용법

```
단축키: Shift + Tab
또는: "Plan Mode로 진입해" / "/plan"
나오기: "이 계획대로 진행해줘"
```

**Before/After:**
- Before: "블로그 만들어줘" → 제네릭
- After: Shift+Tab → 10단계 계획 확인 → "3번 바꿔, 7번 빼" → 정확히 구현

---

## DCR 실전 패턴

### D — Define (정의)
새 기능 시작 전:
```
"PLAN.md §4 핵심 기능 3개 중 [N번째] 기능을 만들려고 해.
Plan Mode로 구현 계획 잡아줘."
```

### C — Converse (쪼개서 대화)
한 번에 너무 많이 시키지 않는다:
```
❌ "로그인+DB+UI+결제 한 번에 만들어줘"
✅ "로그인 폼 UI부터 만들어줘" → 완료 후 → "DB 연결해줘" → ...
```

### R — Refine (정제)
에러 발생 시:
```
에러 메시지 전체 복붙 → "이 에러 어떻게 고칠까?"
스크린샷 첨부 → "이 화면에서 뭐가 문제야?"
```

---

## 10분마다 커밋 (습관 #6)

```bash
git add [파일명]           # git add -A 금지 (시크릿 노출 위험)
git commit -m "feat: 히어로 섹션 완성"
```

커밋 메시지 형식:
- `feat:` 새 기능
- `fix:` 버그 수정
- `style:` 디자인 변경
- `refactor:` 코드 정리

---

## 배포 전 안전 6체크

1. `.env.local`에 모든 키 있는가?
2. `.gitignore`에 `.env*` 포함되어 있는가?
3. Supabase RLS 활성화되어 있는가?
4. Claude API `max_tokens: 500` 고정되어 있는가?
5. 실제 결제 경로 확인했는가? (ainowclass 40분 장애 교훈)
6. localhost에서 실제로 동작하는가?

---

## 배포 4단계 (git push = 배포)

```bash
# 1단계: 커밋
git add [수정된 파일들]
git commit -m "feat: 기능 완성"

# 2단계: 푸시
git push origin main

# 3단계: Vercel 확인 (30초~2분)
# vercel.com 대시보드 → 빌드 완료 확인

# 4단계: 실제 URL에서 동작 확인 (HTTP 200 사고 교훈)
# 상태 코드만 보지 말고, 실제 페이지 열어서 눈으로 확인
```

---

## 고정 스택 6개

> 다른 스택 찾느라 시간 쓰지 말 것. 이 6개로 100% 가능.

| 스택 | 역할 |
|:---|:---|
| Next.js | 프레임워크 (프론트+백엔드) |
| Tailwind | 스타일링 |
| Supabase | DB + 인증 + Storage |
| Claude API | AI 기능 |
| Vercel | 배포 |
| 토스페이먼츠 | 결제 |

> 상세: `../../../knowledge/tech-stack.md`

---

## 검수 기준

| ID | 기준 | 합격 조건 | 가중치 |
|:---|:---|:---|:---:|
| D1 | PLAN.md 존재 | 프로젝트 루트에 있음 | 필수 |
| D2 | .gitignore .env* | 커밋 전 확인 | 필수 |
| D3 | RLS 활성화 | Supabase 설정 확인 | 필수 |
| D4 | 10분마다 커밋 | git log 확인 | 필수 |
| D5 | 배포 후 눈으로 확인 | 실제 URL 직접 열어봄 | 필수 |
