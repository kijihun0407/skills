# SOP: 개발 안전 체크리스트

> "실수는 시스템으로 막는다. lessons.md가 비면 같은 실수 영원히 반복."
> 실제 사고 5건 기반으로 만든 방어 SOP.

---

## 실전 교훈 TOP 5 (실제 사고)

### 사고 #1: ainowclass 40분 장애 (2026-03-24)
- **원인**: "실제로 결제가 일어나는가?" 확인 안 하고 배포
- **결과**: 40분 프로덕션 장애 + 긴급 롤백
- **방어책**: 배포 전 결제 경로 반드시 확인. "이 사이트에서 결제가 실제로 일어나는가?"

### 사고 #2: HTTP 200 사고 (2026-04-14)
- **원인**: HTTP 200으로 "배포 완료" 판정. 실제는 빈 fallback 페이지
- **결과**: 30분 잘못된 상태 운영
- **방어책**: 상태 코드 + 실제 페이지 열어서 눈으로 확인 (3중 체크)

### 사고 #3: .env 줄바꿈 장애 (2026-04-10)
- **원인**: .env 값 붙여넣기 시 줄바꿈 1개 포함
- **결과**: 디스코드 전수 장애
- **방어책**: .env 값 붙여넣기 후 반드시 줄바꿈 제거 확인

### 사고 #4: 시크릿 3주 커밋 (2026-04-11)
- **원인**: `git add -A` 사용으로 .env 파일 실수 커밋
- **결과**: API 키 GitHub에 3주 노출
- **방어책**: `git add -A` 사용 금지. 파일명 명시적으로 추가

### 사고 #5: Supabase SSR 인증 패턴 (2026-02-24)
- **원인**: 공식 SSR 패턴 안 따름
- **방어책**: Supabase 공식 문서의 SSR 인증 패턴 그대로 따르기

---

## API 키 보안 체크리스트

```bash
# ✅ 올바른 방법
ANTHROPIC_API_KEY=sk-ant-...          # 서버 사이드 전용
NEXT_PUBLIC_SUPABASE_URL=...          # 클라이언트 노출 OK
NEXT_PUBLIC_SUPABASE_ANON_KEY=...     # 클라이언트 노출 OK

# ❌ 절대 금지
NEXT_PUBLIC_ANTHROPIC_API_KEY=...     # 클라이언트에 노출 = 해킹 위험
NEXT_PUBLIC_TOSS_SECRET_KEY=...       # 결제 키 노출 = 사고
```

### .gitignore 필수 항목 확인
```
.env
.env.local
.env.*.local
.env.development.local
.env.production.local
```

---

## Claude API 비용 방어선 3개

```javascript
// 필수 설정
const response = await anthropic.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 500,           // ① 토큰 상한
  messages: [{
    role: "user",
    content: userInput.slice(0, 1000)  // ② 입력 1000자 cap
  }]
});

// ③ Rate Limit (미들웨어에서)
// IP당 일 10회 제한
```

---

## Supabase 보안 체크리스트

```sql
-- RLS 활성화 확인 (Supabase 대시보드 > Auth > Policies)
-- 모든 테이블에 RLS 활성화되어 있는가?

-- 기본 RLS 정책 예시
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users can only see own profile"
  ON profiles FOR SELECT
  USING (auth.uid() = user_id);
```

> RLS 비활성화 = 해커 천국. 배포 전 반드시 확인.

---

## 배포 안전 SOP

### 1. 커밋 전 체크
```bash
git diff --name-only      # 변경된 파일 확인
git status                 # 상태 확인
# .env* 파일이 포함되어 있으면 즉시 중단
```

### 2. 커밋 (안전하게)
```bash
git add src/components/Hero.tsx   # 파일명 명시 (git add -A 금지)
git commit -m "feat: 히어로 섹션 추가"
```

### 3. 배포 후 확인 (3중 체크)
```
① HTTP 상태 코드 확인 (200 OK?)
② 실제 페이지 열어서 내용 확인 (빈 페이지 아닌지?)
③ 결제 경로 확인 (실제 결제 플로우 동작하는지?)
```

---

## 검수 기준

| ID | 기준 | 합격 조건 | 가중치 |
|:---|:---|:---|:---:|
| S1 | .gitignore .env* 포함 | git status에서 .env 파일 안 보임 | 필수 |
| S2 | Claude API max_tokens 500 | 코드에서 확인 | 필수 |
| S3 | Supabase RLS 활성화 | 대시보드에서 확인 | 필수 |
| S4 | 배포 후 실제 페이지 확인 | 눈으로 직접 열어봄 | 필수 |
| S5 | git add -A 미사용 | 파일명 명시적 추가 | 필수 |
