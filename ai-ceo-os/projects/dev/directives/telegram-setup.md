# SOP: 텔레그램 연동 — 폰에서 AI에게 지시하기

> 컴퓨터 앞에 없어도 AI가 일한다. 지하철/카페/침대에서 폰으로 AI에게 일을 시킨다.

---

## 2가지 방법 비교

| 구분 | 방법 1: Channels (쉬움) | 방법 2: EC2 서버 (고급) |
|:---|:---|:---|
| 난이도 | ⭐ — 명령어 1줄 | ⭐⭐⭐ — 서버 셋업 |
| 비용 | 추가 0원 (기존 구독만) | 월 ~$38 (EC2) |
| 작동 조건 | 내 PC가 켜져 있어야 함 | 24시간 자동 |
| 추천 | 왕초보 — 오늘 바로 시작 | 자동화 고급자 |

**시작 전략**: 방법 1(Channels)로 먼저 시작. PC가 켜져 있을 때만 되지만 설정이 5분.

---

## 방법 1: Channels (PC 필요, 5분 셋업)

### 사전 준비
- Node.js v18 이상
- npm으로 Claude Code 글로벌 설치
- Bun 런타임
- 텔레그램 앱

### STEP 1: Bun 설치

**Mac/Linux:**
```bash
curl -fsSL https://bun.sh/install | bash
```

**Windows (PowerShell):**
```powershell
irm bun.sh/install.ps1 | iex
```

확인: `bun --version`

### STEP 2: Claude Code 글로벌 설치
```bash
npm install -g @anthropic-ai/claude-code
```
확인: `claude --version`

### STEP 3: 텔레그램 봇 만들기
1. 텔레그램에서 @BotFather 검색 → 대화 시작
2. `/newbot` 입력
3. 봇 이름 입력 (예: `My Claude Bot`)
4. 유저네임 입력 — `bot`으로 끝나야 함 (예: `myclaudeai_bot`)
5. BotFather가 보내주는 **토큰 복사** (형태: `123456789:AAHfiqks...`)

### STEP 4: 플러그인 설치

터미널에서:
```bash
claude
```

Claude Code 세션 안에서:
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install telegram
/reload-plugins
```

### STEP 5: 텔레그램 토큰 등록
```
/telegram:configure
```
→ STEP 3에서 복사한 봇 토큰 입력 → `/exit`

### STEP 6: 텔레그램 채널 모드로 실행
```bash
claude --channels plugin:telegram@claude-plugins-official
```

### STEP 7: 페어링
1. 텔레그램에서 내가 만든 봇에게 DM 전송
2. 봇이 **6자리 페어링 코드** 응답
3. 클로드 코드 터미널에 페어링 코드 입력

→ 연결 완료! 텔레그램으로 Claude Code와 대화 가능

### 단축 명령어 등록 (선택)

Mac (zsh):
```bash
echo 'alias claude-tg="claude --channels plugin:telegram@claude-plugins-official"' >> ~/.zshrc
source ~/.zshrc
```

---

## 방법 2: EC2 서버 (24시간 자동)

### 아키텍처
```
📱 내 폰 (텔레그램)
  → 🤖 텔레그램 봇
       → 🖥️ AWS EC2 (24시간, 월 $38)
            → Claude Code CLI → 스킬/규칙/데이터 전부 적용
                 → 📱 텔레그램으로 결과 전송
```

### 필요한 것 3가지
| 필요한 것 | 비용 | 설명 |
|:---|:---|:---|
| 텔레그램 봇 토큰 | 무료 | @BotFather에게 /newbot → 토큰 발급 |
| AWS EC2 서버 | ~$38/월 | 24시간 서버 |
| Claude Code 구독 | 기존 구독 | 추가 비용 없음 |

### .env 설정 (필수 4줄)
```
TELEGRAM_BOT_TOKEN=여기에_BotFather_토큰
TELEGRAM_BOT_USERNAME=내봇이름
ALLOWED_USERS=내_텔레그램_ID
APPROVED_DIRECTORY=/home/ubuntu/ainow
```

> **ALLOWED_USERS 필수**: 없으면 아무나 내 AI에게 명령 가능. 내 텔레그램 ID는 @userinfobot에게 메시지 보내면 확인 가능.

### 24시간 자동 실행
```bash
sudo systemctl enable claude-telegram
sudo systemctl start claude-telegram
```

---

## 자주 묻는 질문

| 증상 | 원인 및 해결 |
|:---|:---|
| "입력중..."만 뜨고 답이 안 와요 | 봇이 보낸 **6자리 코드**를 터미널에 입력했는지 확인 |
| `claude` 명령어 자체가 안 돼요 | `npm install -g @anthropic-ai/claude-code` 후 새 터미널 |
| 플러그인 설치가 안 돼요 | `/plugin marketplace update claude-plugins-official` 후 재시도 |
| Bun이 없다는 에러 | `bun --version` 확인 후 STEP 1 진행 |

---

## 실제 활용 예시

| 상황 | 보내는 메시지 | AI 응답 |
|:---|:---|:---|
| 카페에서 | "릴스 대본 교육형 3개 써줘" | 대본 3개 완성 |
| 지하철에서 | "오늘 할 일 정리해줘" | 우선순위 투두 리스트 |
| 침대에서 | "내일 미팅 일정 추가해줘" | 캘린더 등록 완료 |
| 이동 중 | "이번 주 광고 성과 어때?" | ROAS/CPA 요약 + 액션 아이템 |
