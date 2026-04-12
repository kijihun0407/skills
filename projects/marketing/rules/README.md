# rules/ — 업무 규칙 정의

> CLAUDE.md에서 `@rules/파일명.md`로 임포트합니다.
> `.claude/rules/`와의 차이: 이 폴더는 명시적 임포트, `.claude/rules/`는 항시 자동 주입.

---

## 파일 구성 가이드

| 파일 | 역할 | 임포트 위치 |
|:-----|:-----|:------------|
| `core.md` | 항시 적용 운영 원칙 | CLAUDE.md 하단 |
| `output.md` | 산출물 저장·형식 규칙 | skills/SKILL.md |
| `quality.md` | 품질 기준선 | 검수 단계 |
| `decision.md` | 의사결정 프레임워크 | 전략 작업 시 |
| `tools.md` | 도구 활용 제안 규칙 | 작업 시작 전 |

---

## `.claude/rules/` vs `rules/` 차이

| 구분 | `.claude/rules/` | `rules/` (이 폴더) |
|:-----|:-----------------|:-------------------|
| 적용 방식 | 하네스 자동 주입 (system-reminder) | CLAUDE.md에서 명시적 `@import` |
| 사용 시점 | 항시 | 필요한 맥락에서만 |
| 용도 | 절대 규칙, 안전장치 | 업무별 상황 규칙 |

---

## 등록된 규칙 파일

- `core.md` — 핵심 운영 원칙 (Zero-Inference, 무중단 실행, 직언, KPI)
- `금지행동.md` — 절대 금지 4개 조항 + 모든 작업 전 자동 체크
