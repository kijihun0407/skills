# 캐러셀 디자인 가이드 — @Grab_Prompt 표준

> 기준 파일: `.tmp/carousel_assets/carousel_ai_research.html` (AI 연구 데이터 유통기한 — 확정본)

---

## 기본 스펙

| 항목 | 값 |
|------|-----|
| 슬라이드 크기 | 1080×1080px (1:1 정사각형) |
| 슬라이드 수 | 7장 (커버 1 + 본문 5 + CTA 1) |
| 제작 방식 | HTML/CSS → Playwright PNG 자동 추출 |
| 추출 스크립트 | `.tmp/carousel_assets/export_slides.js` |
| 업로드 | slide_01.png ~ slide_07.png 순서대로 인스타 캐러셀 |

---

## 폰트

```css
font-family: 'Noto Sans KR', 'Inter', sans-serif;
/* Google Fonts CDN 링크 필수 */
```

---

## 커버 슬라이드 (1장) 구조

배경·인물·텍스트를 레이어로 쌓는 방식:

```
[Layer 0] bg-paper    — 주제 관련 이미지/논문/자료 사진, blur(4px) brightness(0.18)
[Layer 1] person-photo — 인물 사진, 오른쪽 배치, 좌측·하단 가장자리 mask 페이드
[Layer 2] paper-card   — 보조 자료 이미지 1 (오른쪽 상단, 가장자리 페이드)
[Layer 3] tweet-card   — 보조 자료 이미지 2 (오른쪽 하단, 가장자리 페이드)
[Layer 4] grad-left    — 좌→우 어두운 그라디언트 (텍스트 가독성)
[Layer 5] grad-bottom  — 하→상 그라디언트
[Layer 6] tag          — 상단 좌측 카테고리 태그
[Layer 7] content      — 하단 좌측 헤드라인 + 서브텍스트
```

### 커버 핵심 CSS 패턴

```css
/* 배경 자료 이미지 */
.s1 .bg-paper {
  position:absolute; inset:0;
  background:url('./자료이미지.jpeg') center/cover no-repeat;
  filter:blur(4px) brightness(0.18);
  transform:scale(1.06);
}

/* 인물 사진 — 우측, 가장자리 페이드 */
.s1 .person-photo {
  position:absolute;
  right:240px; top:0; bottom:0;
  width:520px; height:100%;
  object-fit:cover; object-position:center top;
  -webkit-mask-image:
    linear-gradient(to right, transparent 0%, black 10%, black 92%, transparent 100%),
    linear-gradient(to bottom, black 0%, black 88%, transparent 100%);
  -webkit-mask-composite: destination-in;
  mask-image:
    linear-gradient(to right, transparent 0%, black 10%, black 92%, transparent 100%),
    linear-gradient(to bottom, black 0%, black 88%, transparent 100%);
  mask-composite: intersect;
}

/* 보조 이미지 공통 — 우측 absolute, 가장자리 페이드 */
.s1 .paper-card {
  position:absolute;
  right:0; top:60px;
  width:290px; height:370px;
  object-fit:cover; object-position:top;
  -webkit-mask-image:
    linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%),
    linear-gradient(to bottom, transparent 0%, black 8%, black 90%, transparent 100%);
  -webkit-mask-composite: destination-in;
  mask-image:
    linear-gradient(to right, transparent 0%, black 10%, black 90%, transparent 100%),
    linear-gradient(to bottom, transparent 0%, black 8%, black 90%, transparent 100%);
  mask-composite: intersect;
}

/* 헤드라인 — 하단 좌측 */
.s1 .content {
  position:absolute;
  bottom:185px; left:72px;
  width:580px; z-index:10;
}
.s1 .headline {
  font-size:96px; font-weight:900; color:#FFFFFF;
  line-height:1.05; letter-spacing:-0.03em; word-break:keep-all;
}
.s1 .headline em { font-style:normal; color:#60A5FA; }
```

---

## 본문 슬라이드 (2~6장) 구조

### 짝수 슬라이드 — 다크 테마 (#0A1628)
- 배경: 네이비 다크 + 격자 오버레이
- 텍스트: 흰색/연파랑
- 우측에 자료 이미지(있을 경우): absolute 배치, `border-radius:16px`, 블러 없음
- 이미지 있을 경우 텍스트 우측 여백 400px 확보

### 홀수 슬라이드 — 라이트 테마 (#FFFFFF)
- 상단 포인트 컬러 accent bar (6px)
- 텍스트: 다크 (#0A1628)
- 우측 이미지 동일 방식

### 우측 이미지 배치 (자료/원문 있을 때)

```css
.wrap {
  position:absolute;
  right:36px; top:50%; transform:translateY(-50%);
  width:330px; z-index:4;
  display:flex; flex-direction:column; align-items:center; gap:18px;
}
.wrap img {
  width:330px; height:460px;
  object-fit:cover; object-position:top;
  border-radius:16px;
}
.wrap .caption {
  font-size:20px; font-weight:500; color:rgba(255,255,255,0.45);
  text-align:center; font-style:italic;
}
```

---

## CTA 슬라이드 (7장) 구조

- 배경: 흰색
- 상단 accent bar (파란색)
- "무료 자료 제공" 라벨
- 헤드라인 (체크리스트 전문 DM으로 드려요)
- 댓글 키워드 박스: `"체크"` → DM 자동 발송
- 팔로우 후 댓글 안내

---

## 색상 시스템

```css
/* 다크 슬라이드 */
--dark-bg:    #0A1628
--dark-text:  #FFFFFF
--dark-muted: #9CA3AF
--accent:     #1D6FEB   /* 파란색 포인트 */
--accent-lt:  #60A5FA

/* 라이트 슬라이드 */
--light-bg:   #FFFFFF
--light-text: #0A1628
--light-sub:  #4B5563

/* 위험/강조 */
--red:        #EF4444
--yellow:     #FCD34D
```

---

## 공통 요소

```css
/* 푸터 — 모든 슬라이드 */
.footer {
  position:absolute;
  bottom:52px; left:72px; right:72px;
  display:flex; align-items:center; justify-content:space-between;
}
/* @Grab_Prompt | 01 / 07 */

/* 태그 pill */
.tag {
  display:inline-flex; align-items:center;
  font-size:20px; font-weight:700;
  letter-spacing:0.14em; text-transform:uppercase;
  padding:10px 24px; border-radius:100px;
}
```

---

## 제작 SOP

1. `.tmp/carousel_assets/carousel_ai_research.html` 복사 → `carousel_[주제].html`
2. 필요한 이미지를 `.tmp/carousel_assets/`에 복사
3. 슬라이드별 텍스트·색상·이미지 교체
4. 브라우저로 열어 확인
5. `node export_slides.js` 실행 → 7장 PNG 자동 추출
6. 캡션 md 파일 작성 → `outputs/2026/MM/DD/[캐러셀]_주제.md`
7. slide_01 ~ 07 + 캡션으로 인스타 업로드

---

## 참고 파일
- 확정 템플릿: `.tmp/carousel_assets/carousel_ai_research.html`
- PNG 추출 스크립트: `.tmp/carousel_assets/export_slides.js`
