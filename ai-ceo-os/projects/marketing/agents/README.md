# agents/ — 마케팅 사업부 담당 임원

> @참조 패턴: 본사 C-Suite 원본을 복사하지 않고 경로로 연결.
> 본사에서 임원 페르소나 업데이트 시 이 사업부에 자동 반영.

---

## 담당 임원 (2명)

### CCO (콘텐츠 최고 책임자)
- 본사 경로: `@../../../agents/cco/README.md`
- 로컬 페르소나: `cco.md` (마케팅 사업부 특화 역할 정의)
- 이 사업부에서의 추가 역할:
  - 릴스/카드뉴스 대본 기획 및 검수
  - 채널 규칙(`context/channel-rules.md`) 자동 참조
  - 레퍼런스 크리에이터 벤치마크 비교

### CMO (마케팅 최고 책임자)
- 본사 경로: `@../../../agents/cmo/README.md`
- 로컬 페르소나: `cmo.md` (마케팅 사업부 특화 역할 정의)
- 이 사업부에서의 추가 역할:
  - CTA/해시태그 전환 관점 검증
  - 팔로워 → 유료 상품 전환 퍼널 설계
  - 도구 스택 ROI 판단 (ad-revenue.md 참조)

---

## 소집 기준

| 작업 | 소집 임원 |
|:---|:---|
| 릴스 대본 · 카드뉴스 기획 | CCO 단독 |
| 전환 전략 · 광고 검토 | CMO 단독 |
| 주간 콘텐츠 캘린더 전략 | CCO + CMO |
| 레퍼런스 분석 + 차별화 | CCO + CMO |

---

## 연결 구조

```
본사 agents/cco/ ──→ marketing/agents/cco.md (추가 역할 정의)
본사 agents/cmo/ ──→ marketing/agents/cmo.md (추가 역할 정의)
```

> 본사 C-Suite 전체 프로토콜: `../../../agents/c-suite-protocol.md`
