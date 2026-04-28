# 캐러셀 디자인 가이드 — @ai.saver_ 표준

> 이 가이드를 기준으로 모든 캐러셀을 제작합니다.
> 참고 파일: `.tmp/carousel_assets/carousel_gpt55.html` (GPT-5.5 기능 — 1호 확정본)

---

## 기본 스펙

| 항목 | 값 |
|------|-----|
| 슬라이드 크기 | 1080×1350px (4:5 비율 — 인스타 최적) |
| 브라우저 표시 | 50% 축소 (540×675px 프리뷰) |
| 슬라이드 수 | 7장 (커버 1 + 본문 4~5 + CTA 1) |
| 제작 방식 | HTML/CSS → 슬라이드별 스크린샷 → 인스타 캐러셀 업로드 |

---

## 색상 시스템 (다크 테마)

```css
/* 배경 */
--bg-main:    #080810   /* 슬라이드 기본 배경 */
--bg-body:    #020208   /* 브라우저 배경 */

/* 텍스트 */
--text-white:  #FFFFFF
--text-muted:  rgba(255,255,255,0.62)
--text-dim:    rgba(255,255,255,0.28)

/* 포인트 컬러 (슬라이드별 구분) */
--yellow:  #FBBF24   /* 커버, 기본 강조 */
--purple:  #8B5CF6   /* 기능 2 */
--blue:    #3B82F6   /* 기능 3 */
--green:   #10B981   /* 기능 4 */
```

---

## 공통 레이아웃 규칙

### 상단 계정 배지 (모든 슬라이드 고정)
```css
position: absolute;
top: 48px; 좌우 중앙;
background: rgba(255,255,255,0.07);
border: 1.5px solid rgba(255,255,255,0.14);
font-size: 26px; font-weight: 800;
padding: 12px 44px; border-radius: 50px;
```
표시 텍스트: `@ai.saver_`

### 페이지 번호 (모든 슬라이드 고정)
```css
position: absolute;
bottom: 48px; right: 64px;
color: rgba(255,255,255,0.28);
font-size: 24px; font-weight: 600;
```
표시 형식: `01 / 07`

### 여백 기준
- 좌우 기본 여백: `80px`
- 상단 컨텐츠 시작: `150px` (배지 아래)

---

## 슬라이드별 구성

### 1장 — 커버
- 상단: 카테고리 뱃지 (골드 테두리 pill)
- 중앙: 메인 제목 (대형 숫자/키워드 골드 그라디언트)
- 하단: 기능 태그 모음 + 서브텍스트
- 배경: 골드 + 블루 글로우 장식

### 2~5장 — 기능/본문 슬라이드
- 배경 왼쪽 하단: 대형 반투명 번호 (장식)
- 상단 좌측: 번호 박스(포인트 컬러) + "카테고리" 레이블
- 우측: 이모지 아이콘 박스 (포인트 컬러 테두리)
- 제목: main(흰색) + sub(포인트 컬러)
- 구분선 후 본문 설명 3줄
- 하단: 실전 TIP 박스 (포인트 컬러 반투명 배경)

### 마지막 CTA 슬라이드
- "유용했다면 💾" 상단
- 대형 메인 문구
- 내용 요약 리스트 (포인트 박스)
- `@ai.saver_` 골드 그라디언트 계정명

---

## 폰트 시스템

```css
font-family: 'Pretendard', -apple-system, 'Apple SD Gothic Neo', sans-serif;

/* 커버 대형 숫자/키워드 */  font-size: 130px; font-weight: 900;

/* 슬라이드 제목 main */     font-size: 58px;  font-weight: 900;
/* 슬라이드 제목 sub */      font-size: 27px;  font-weight: 700;
/* 본문 설명 */              font-size: 29px;  font-weight: 500; line-height: 1.85;
/* TIP 박스 */               font-size: 27px;  font-weight: 700;
/* 페이지 번호 */             font-size: 24px;  font-weight: 600;
```

---

## 네비게이션
- 좌/우 화살표 버튼 + 하단 도트 인디케이터
- 키보드 `←` `→` 지원
- 도트 활성화: 골드(`#FBBF24`) + 가로로 늘어남

---

## 제작 SOP

1. 이 가이드 참고 → HTML 파일 생성 (`carousel_[주제].html`)
2. 저장 위치: `.tmp/carousel_assets/`
3. 브라우저로 열기 → 슬라이드별 스크린샷 (고화질: 브라우저 줌 200%)
4. 7장 이미지 → 인스타그램 캐러셀 업로드
5. 캡션 + 해시태그 첨부

---

## 참고 파일
- 1호 확정본: `.tmp/carousel_assets/carousel_gpt55.html` (GPT-5.5 직장인 필수 기능)
- 캐러셀 대본: `outputs/2026/04/25/[캐러셀]_이번주_캐러셀2종_대본+CSV.md`
