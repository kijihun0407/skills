# DESIGN.md — 내 프로젝트 디자인 가이드

> **기본 템플릿** (Linear 스타일, 미니멀 다크모드).
> 취향 맞으면 그대로 사용, 바꾸고 싶으면 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)에서 66+ 개 중 1개 골라 교체.

---

## 🎨 디자인 철학

- **미니멀리즘** — 요소는 적게, 여백은 많게
- **타이포 중심** — 텍스트가 주인공
- **생산성 도구 톤앤매너** — Linear / Notion / Vercel 스타일
- **다크모드 우선** — 개발자/크리에이터 대상

---

## 🎨 컬러 팔레트

### 다크 테마 (기본)
```css
--bg-primary: #131316;      /* 메인 배경 */
--bg-secondary: #1C1C21;    /* 카드/섹션 배경 */
--bg-elevated: #25252B;     /* 모달/드롭다운 */
--border: #2F2F36;          /* 테두리 */
--text-primary: #F5F5F7;    /* 메인 텍스트 */
--text-secondary: #A1A1AA;  /* 보조 텍스트 */
--text-muted: #71717A;      /* 비활성 텍스트 */
--accent: #5E6AD2;          /* Linear 블루 */
--accent-hover: #7982DE;
--success: #26D07C;
--warning: #F59E0B;
--error: #EF4444;
```

### 라이트 테마 (옵션)
```css
--bg-primary: #FFFFFF;
--bg-secondary: #F5F5F7;
--bg-elevated: #FFFFFF;
--border: #E4E4E7;
--text-primary: #18181B;
--text-secondary: #52525B;
--text-muted: #A1A1AA;
--accent: #5E6AD2;
```

---

## 📝 타이포그래피

### 폰트 패밀리
```css
--font-sans: "Pretendard", "Inter", -apple-system, sans-serif;
--font-mono: "JetBrains Mono", "Fira Code", monospace;
```

### 계층
- **H1 (히어로)**: 48px / 600 weight / -0.02em letter-spacing
- **H2 (섹션)**: 32px / 600 weight
- **H3 (서브섹션)**: 24px / 600 weight
- **Body**: 16px / 400 weight / 1.6 line-height
- **Caption**: 14px / 400 weight / #A1A1AA
- **Label**: 13px / 500 weight / uppercase / 0.05em letter-spacing

---

## 📐 레이아웃

### 간격 시스템 (4px 기준)
```
xs:  4px
sm:  8px
md:  16px
lg:  24px
xl:  32px
2xl: 48px
3xl: 64px
4xl: 96px
```

### 컨테이너
- 최대 너비: **1200px** (메인 콘텐츠)
- 사이드 여백: **24px** (모바일) / **48px** (데스크탑)
- 섹션 간격: **96px** (큰 섹션) / **64px** (일반)

### 그리드
- 12컬럼 그리드 (flex 또는 grid)
- 모바일 브레이크포인트: **768px**
- 태블릿: **1024px**
- 데스크탑: **1280px**

---

## 🎁 컴포넌트 스타일

### 버튼 (Primary)
```css
background: var(--accent);
color: white;
padding: 10px 16px;
border-radius: 6px;
font-weight: 500;
font-size: 14px;
transition: background 0.15s ease;

&:hover { background: var(--accent-hover); }
&:active { transform: scale(0.98); }
```

### 카드
```css
background: var(--bg-secondary);
border: 1px solid var(--border);
border-radius: 8px;
padding: 24px;
```

### 입력 필드
```css
background: var(--bg-secondary);
border: 1px solid var(--border);
border-radius: 6px;
padding: 8px 12px;
font-size: 14px;
color: var(--text-primary);

&:focus {
  border-color: var(--accent);
  outline: 2px solid rgba(94, 106, 210, 0.2);
}
```

---

## 🎬 모션

### 기본 트랜지션
```css
transition: all 0.15s ease;
```

### 호버
- 버튼: background 변화 + `scale(1.02)` (옵션)
- 카드: `translateY(-2px)` + 그림자 약간 강화

### 페이지 로드
- fade in (opacity 0 → 1, 400ms)
- 스태거 (0.05s 간격으로 순차 등장)

---

## 🌗 다크모드 토글

```tsx
// Tailwind 기준
<html className={darkMode ? 'dark' : ''}>
```

**다크모드가 기본**, 라이트모드는 옵션.

---

## 🚫 디자인 금지사항 (의도적 결핍)

1. ❌ 그라디언트 남용 (생산성 톤에서 벗어남)
2. ❌ 이모지 아이콘 (Linear 톤에 안 맞음 — 아이콘은 `lucide-react` 사용)
3. ❌ 5개 이상 컬러 사용 (미니멀리즘 위반)
4. ❌ 애니메이션 길이 500ms 초과 (생산성 체감 저하)
5. ❌ Serif 폰트 (생산성 톤에 부적합)

---

## 💡 AI에게 이 DESIGN.md 활용시키기

```
이 프로젝트의 DESIGN.md를 참고해서 히어로 섹션을 만들어줘.
- 컬러는 --bg-primary, --text-primary만 사용
- 타이포는 H1 + body만
- 버튼은 Primary 스타일
- 모바일 반응형 (768px 기준)
```

→ AI가 자동으로 **Linear 스타일의 일관된 UI** 생성.

---

## 🔗 참고

- **기본 영감**: Linear.app
- **컬러 레퍼런스**: Stripe, Vercel, Supabase
- **다른 옵션**: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) 에 66+ 브랜드 템플릿

---

## 📝 커스터마이징 체크리스트

- [x] 브랜드 컬러 1개로 `--accent` 교체
      → `#5E6AD2` (Linear Blue) 유지. AI 툴 신뢰감 + 기술 전문성 느낌. 비전공자 타겟에게도 "AI스러운" 인상 전달.
- [x] 로고 폰트 선택
      → **Pretendard** (한국 사용자 최적화, 가독성 최고, 비전공자 친화)
- [x] 다크/라이트 중 기본값 선택
      → **라이트모드 기본** (비전공자 타겟 — 다크모드보다 접근성 높음. 두려움 제거가 핵심 가치이므로 밝고 친근한 톤 우선)
      → 다크 토글 옵션은 유지
- [x] 내 서비스 톤앤매너에 맞는 컴포넌트 활성화
      → 히어로 섹션 (Before/After 비교) + 이메일 입력 폼 + CTA 버튼 (Primary) + 신뢰 카드 3개 + 업셀 섹션
