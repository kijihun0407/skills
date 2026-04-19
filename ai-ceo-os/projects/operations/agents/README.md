# agents/ — 운영 사업부 담당 임원

> @참조 패턴: 본사 C-Suite 원본을 복사하지 않고 경로로 연결.
> 본사에서 임원 페르소나 업데이트 시 이 사업부에 자동 반영.

---

## 담당 임원 (1명)

### COO (운영 최고 책임자)
- 본사 경로: `@../../../agents/coo/README.md`
- 로컬 페르소나: `coo.md` (운영 사업부 특화 역할 정의)
- 이 사업부에서의 추가 역할:
  - 직장+부업 병행 루틴 설계 및 번아웃 방지
  - 주간 브리핑 (`directives/weekly-briefing.md`) 실행
  - 수익화 로드맵 진척 추적 (`directives/monetization-roadmap.md`)

---

## 소집 기준

| 작업 | 소집 임원 |
|:---|:---|
| 주간 브리핑 · 루틴 점검 | COO 단독 |
| 업무 자동화 판단 | COO 단독 |
| 수익화 60일 로드맵 리뷰 | COO + 본사 CFO |
| 사업부 간 조율 | COO + 본사 CSO |

---

## 연결 구조

```
본사 agents/coo/ ──→ operations/agents/coo.md (추가 역할 정의)
```

> 본사 C-Suite 전체 프로토콜: `../../../agents/c-suite-protocol.md`
