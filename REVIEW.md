# 게시 전 검토 목록 (REVIEW)

이 사이트의 문구는 모두 새로 쓴 초안입니다. 게시(공개 저장소 푸시, GitHub Pages 켜기) 전에 아래 항목을 확인해 주세요. 확인한 항목은 `[x]`로 바꾸면 됩니다.

작성 원칙: 제품 설명은 제품 이름과 분류에서만 끌어냈고, 고객사·인증·성능 수치·가격·"최초/최고" 같은 확인할 수 없는 주장은 넣지 않았습니다. 사실과 다르거나 범위가 넓게 읽히는 표현이 있으면 고쳐 주세요.

## 1. 사업자 정보 (모든 페이지 바닥글)

- [ ] **사업자등록번호: `447-32-01209`** — 사업자등록증 이미지(`D:\dev\Onnode\www\사업자등록증.png`)의 "등록번호"에서 읽었습니다. 원본과 한 번 더 대조해 주세요.
- [ ] 회사명: 온노드 (OnNode)
- [ ] 대표: 오해란
- [ ] 주소: 서울특별시 서대문구 북아현로 90-7, 2층(북아현동)
- [ ] 전화: `000-0000-0000` — **자리표시입니다. 실제 번호로 바꿔야 합니다.**
- [ ] 이메일: oonnode@gmail.com
- [ ] 업태: 도매 및 소매업, 임대서비스업 (요청하신 문구 그대로. 등록증에는 "임대 서비스업"으로 띄어 쓰여 있음)
- [ ] 종목: 컴퓨터 및 주변장치, 소프트웨어 도매업
- [ ] 저작권 표기: © 2026 OnNode.

## 2. 공통

- [ ] 머리글 메뉴: 솔루션 / 앱 / 견적 요청
- [ ] 바닥글 메뉴: 솔루션 / 견적 요청 / 원투동 / 원투동 지원 / 원투동 개인정보처리방침
- [ ] 브라우저 탭 제목과 검색·공유 설명(meta description, og:description)

| 페이지 | 제목 | 설명 |
|---|---|---|
| 첫 화면 | 온노드 OnNode \| 소프트웨어 라이브러리·솔루션 공급, 오픈소스 구축·기술지원 | 온노드(OnNode)는 소프트웨어 라이브러리와 솔루션을 공급하고, 오픈소스를 이용한 시스템 구축과 기술지원을 합니다. |
| 솔루션 | 솔루션 \| 온노드 OnNode | 온노드의 라이브러리(Delphi, JavaScript/TypeScript), APM, OTP, 리포팅, 서버접근제어, 오픈소스·협업 솔루션 구축/지원과 기술지원 목록입니다. |
| 견적 요청 | 견적 요청 \| 온노드 OnNode | 온노드 제품 공급, 기능 개발, 시스템 구축과 기술지원 견적을 이메일로 요청하실 수 있습니다. |
| 원투동 | 원투동 – 베트남 돈 계산기 \| 온노드 OnNode | 원투동은 베트남 여행 중 현금 지불과 거스름돈 계산, 환율 확인, 현금 가계부 기록을 돕는 앱입니다. 오프라인 우선, 광고·회원가입 없음. |
| 원투동 개인정보처리방침 | 원투동 개인정보처리방침 (초안) \| 온노드 OnNode | 원투동 – 베트남 돈 계산기 앱의 개인정보처리방침입니다. |
| 원투동 지원 | 원투동 지원 · 자주 묻는 질문 (초안) \| 온노드 OnNode | 원투동 – 베트남 돈 계산기 앱의 사용 안내와 문의 방법입니다. |

## 3. 첫 화면 (`index.html`)

- [ ] 큰 제목: 소프트웨어 라이브러리와 솔루션을 공급하고, 오픈소스 시스템을 구축합니다
- [ ] 소개 문단: 온노드는 업무용 소프트웨어 개발에 쓰는 라이브러리와 솔루션을 공급하고, 오픈소스를 이용한 시스템 구축과 기술지원을 합니다. 필요한 항목과 범위를 알려 주시면 확인한 뒤 견적을 보내 드립니다.
- [ ] 버튼: 견적 요청 / 솔루션 보기
- [ ] 솔루션 영역 제목·링크: 솔루션 / 전체 목록 보기 (분류 카드 요약 문구는 아래 4번에 함께 적음)
- [ ] 앱 영역: 원투동 – 베트남 돈 계산기 / "베트남 여행 중 현금으로 낼 돈과 거스름돈을 계산하고, 환율을 확인하고, 쓴 현금을 기록하는 앱입니다. 온노드가 만들고 배포합니다." / 버튼: 앱 소개, 원투동 지원
- [ ] 마지막 영역: 견적 요청 / "제품 공급, 기능 개발, 시스템 구축과 기술지원 견적은 이메일로 받고 있습니다." / 버튼: 견적 요청하기

## 4. 솔루션 (`solutions/index.html`)

- [ ] 소개 문단: 온노드가 공급하는 라이브러리와 솔루션, 구축과 기술지원 서비스입니다. 항목마다 견적을 요청할 수 있습니다.
- [ ] 분류 이름 변경: "오픈소스 구축/지원" 대신 **"오픈소스·협업 솔루션 구축/지원"** (Jira / Confluence / Bitbucket은 오픈소스가 아니므로)
- [ ] 페이지 맨 아래 상표 안내: Delphi, FastReport, 한글(HWP), shadcn/ui, GitLab, Jira, Confluence, Bitbucket, Mattermost, Warpgate, Kubernetes, Proxmox, RustDesk, Redis, Kafka, Java, JavaScript 등 제3자 제품명은 각 권리자의 상표이며, 제품을 구분하기 위해서만 표기했습니다.
- [ ] 각 제품의 `견적 요청` 버튼은 `../quote/?item=<slug>`로 이동하고, 견적 페이지에서 해당 항목이 미리 선택됩니다. 아래 "견적 선택지"는 견적 페이지 선택 상자와 메일 제목에 들어가는 이름입니다.

### 제품별 설명 한 줄

#### 라이브러리 (`solutions/#library`)

- [ ] 첫 화면 카드 요약: Delphi, JavaScript / TypeScript
- [ ] **Delphi / HWP Core Library by OnNode** — Delphi에서 한글(HWP) 문서 형식을 다루기 위한 기반 라이브러리  
      견적 선택지: HWP Core Library by OnNode · slug `hwp-core-library`
- [ ] **Delphi / FastReport Hancom Exports by OnNode** — FastReport 보고서를 HWP·HWPX 형식으로 저장하는 내보내기 기능 (HWP Core Library 포함)  
      견적 선택지: FastReport Hancom Exports by OnNode · slug `fastreport-hancom-exports`
- [ ] **Delphi / 기능 개발 요청 견적** — 필요한 Delphi 기능과 범위를 알려 주시면 개발 견적을 드립니다.  
      견적 선택지: Delphi 기능 개발 요청 · slug `delphi-custom-development`
- [ ] **JavaScript / TypeScript / Beautiful UI System** — 웹 화면을 일관된 규칙으로 만들기 위한 UI 디자인 시스템  
      견적 선택지: Beautiful UI System · slug `beautiful-ui-system`
- [ ] **JavaScript / TypeScript / Beautiful UI Components** — shadcn/ui 기반 UI 컴포넌트 모음  
      견적 선택지: Beautiful UI Components · slug `beautiful-ui-components`
- [ ] **JavaScript / TypeScript / OnNode Grid** — 웹 애플리케이션용 데이터 그리드 컴포넌트  
      견적 선택지: OnNode Grid · slug `onnode-grid`
- [ ] **JavaScript / TypeScript / OnNode Upload** — 웹 애플리케이션용 파일 업로드 컴포넌트  
      견적 선택지: OnNode Upload · slug `onnode-upload`

#### OnNode 이음 (`solutions/#ieum`)

- [ ] 첫 화면 카드 요약: Alt Text System
- [ ] **Alt Text System** — 이미지 대체 텍스트(alt text)를 작성하고 관리하기 위한 시스템  
      견적 선택지: OnNode 이음 – Alt Text System · slug `alt-text-system`

#### APM (`solutions/#apm`)

- [ ] 첫 화면 카드 요약: OnNode Pulse
- [ ] **OnNode Pulse** — 애플리케이션 성능 모니터링(APM) 솔루션  
      견적 선택지: OnNode Pulse · slug `onnode-pulse`

#### UI Builder (`solutions/#ui-builder`)

- [ ] 첫 화면 카드 요약: EV IDE (Enterprise Visual IDE)
- [ ] **EV IDE (Enterprise Visual IDE)** — 업무 화면을 시각적으로 구성하는 UI 빌더  
      견적 선택지: EV IDE (Enterprise Visual IDE) · slug `ev-ide`

#### OTP (`solutions/#otp`)

- [ ] 첫 화면 카드 요약: OnNode OTP: Simple OTP Library, Enterprise OTP System
- [ ] **OnNode OTP / Simple OTP Library** — 애플리케이션에 일회용 비밀번호(OTP) 인증을 붙이기 위한 라이브러리  
      견적 선택지: OnNode OTP – Simple OTP Library · slug `onnode-otp-simple`
- [ ] **OnNode OTP / Enterprise OTP System** — 조직 단위로 OTP 인증을 운영하기 위한 시스템  
      견적 선택지: OnNode OTP – Enterprise OTP System · slug `onnode-otp-enterprise`

#### Reporting Tool (`solutions/#reporting`)

- [ ] 첫 화면 카드 요약: OnNode Report: Viewer, Designer, Data API Server, Reporting Server
- [ ] **OnNode Report / Viewer** — 보고서를 화면에서 보고 출력하는 뷰어  
      견적 선택지: OnNode Report – Viewer · slug `onnode-report-viewer`
- [ ] **OnNode Report / Designer** — 보고서 양식을 만드는 디자이너  
      견적 선택지: OnNode Report – Designer · slug `onnode-report-designer`
- [ ] **OnNode Report / Data API Server (API)** — 보고서에 쓸 데이터를 API로 제공하는 서버  
      견적 선택지: OnNode Report – Data API Server (API) · slug `onnode-report-data-api`
- [ ] **OnNode Report / Reporting Server (Web, JavaScript, Java)** — Web·JavaScript·Java 환경에서 보고서를 생성해 제공하는 서버  
      견적 선택지: OnNode Report – Reporting Server (Web, JavaScript, Java) · slug `onnode-report-server`

#### 서버접근제어 (`solutions/#server-access`)

- [ ] 첫 화면 카드 요약: OnNode Gate
- [ ] **OnNode Gate** — 서버 접근을 통제하기 위한 서버접근제어 솔루션  
      견적 선택지: OnNode Gate · slug `onnode-gate`

#### 오픈소스·협업 솔루션 구축/지원 (`solutions/#open-source`)

- [ ] 분류 안내 문구: 아래 오픈소스와 협업 도구의 설치·구성과 운영 지원을 제공합니다.
- [ ] 첫 화면 카드 요약: GitLab, Jira / Confluence / Bitbucket, Mattermost, Warpgate, Kubernetes, Proxmox, RustDesk, Redis / Kafka
- [ ] **GitLab** — 소스 코드 저장소와 CI/CD 플랫폼  
      견적 선택지: GitLab 구축/지원 · slug `gitlab`
- [ ] **Jira / Confluence / Bitbucket** — 이슈 관리, 문서 협업, 코드 저장소 도구  
      견적 선택지: Jira / Confluence / Bitbucket 구축/지원 · slug `jira-confluence-bitbucket`
- [ ] **Mattermost** — 팀 메신저  
      견적 선택지: Mattermost 구축/지원 · slug `mattermost`
- [ ] **Warpgate** — 서버 접속을 중계하는 배스천(bastion) 호스트  
      견적 선택지: Warpgate 구축/지원 · slug `warpgate`
- [ ] **Kubernetes** — 컨테이너 오케스트레이션 플랫폼  
      견적 선택지: Kubernetes 구축/지원 · slug `kubernetes`
- [ ] **Proxmox** — 서버 가상화 플랫폼  
      견적 선택지: Proxmox 구축/지원 · slug `proxmox`
- [ ] **RustDesk** — 원격 데스크톱 도구  
      견적 선택지: RustDesk 구축/지원 · slug `rustdesk`
- [ ] **Redis / Kafka** — 인메모리 데이터 저장소와 메시지 스트리밍 플랫폼  
      견적 선택지: Redis / Kafka 구축/지원 · slug `redis-kafka`

#### 기술지원 (`solutions/#tech-support`)

- [ ] 첫 화면 카드 요약: 오픈소스 기술지원 서비스팩, 오픈소스를 이용한 시스템 구축
- [ ] **오픈소스 기술지원 서비스팩 (1개월)** — 1개월 단위 오픈소스 기술지원  
      견적 선택지: 오픈소스 기술지원 서비스팩 (1개월) · slug `support-pack-1m`
- [ ] **오픈소스 기술지원 서비스팩 (1년)** — 1년 단위 오픈소스 기술지원  
      견적 선택지: 오픈소스 기술지원 서비스팩 (1년) · slug `support-pack-1y`
- [ ] **오픈소스를 이용한 시스템 구축** — 구축 범위와 요구 사항을 알려 주시면 견적을 드립니다.  
      견적 선택지: 오픈소스를 이용한 시스템 구축 · slug `open-source-system-build`

## 5. 견적 요청 (`quote/index.html`)

- [ ] 소개 문단: 제품 공급, 기능 개발, 시스템 구축과 기술지원 견적을 요청하실 수 있습니다.
- [ ] 안내 문구: 온라인 접수는 준비 중입니다. 아래 항목을 이메일로 보내 주세요.
- [ ] 버튼: 이메일로 견적 요청 (`mailto:oonnode@gmail.com`, 제목 `[견적 요청]`, 본문에 요청자·회사·전화번호·이메일·항목·내용 칸)
- [ ] 보조 문구: 받는 주소 / 메일 제목: [견적 요청] / 버튼을 눌러도 메일 앱이 열리지 않으면 위 주소로 직접 보내 주세요.
- [ ] 메일에 적어 주실 항목: 요청자, 회사, 전화번호, 이메일, 항목, 내용
- [ ] 비활성 양식 제목·설명: 온라인 견적 요청 양식 (준비 중) / 이 양식은 아직 접수되지 않습니다. 같은 내용을 이메일로 보내 주세요.
- [ ] 비활성 버튼: 온라인 접수 준비 중
- [ ] 선택 상자 첫 항목과 마지막 항목: "항목을 선택하세요", "기타 / 아직 정하지 않음"

## 6. 원투동 앱 소개 (`apps/wontodong/index.html`)

- [ ] 제목: 원투동 – 베트남 돈 계산기
- [ ] 소개: 베트남 여행 중 현금으로 낼 돈과 거스름돈을 계산하고, 환율을 확인하고, 쓴 현금을 기록하는 앱입니다.
- [ ] 주요 기능
  - [ ] 현금 지불·거스름돈 계산 — 계산대 앞에서 낼 지폐와 받을 거스름돈을 계산합니다.
  - [ ] 환율 — 원화(KRW)와 베트남 동(VND) 금액을 환율로 바꿔 계산합니다.
  - [ ] 현금 가계부 — 여행 중 현금으로 쓴 돈을 일자별로 기록합니다.
  - [ ] 오프라인 우선 — 마지막으로 받은 환율과 기기에 저장한 기록으로, 인터넷 연결 없이도 계산과 기록을 할 수 있습니다. (PRD의 "환율 캐시 + 로컬 DB로 인터넷 없이 모든 기능 동작"에 맞춤)
  - [ ] 광고·회원가입 없음 — 광고가 없고, 가입 없이 바로 씁니다.
- [ ] 내려받기: Android 테스트 버전은 apps.sicmy.com/wontodong에서 배포하고 있습니다. 앱 스토어 출시는 이후에 안내합니다. / 버튼: Android 테스트 버전 받기 (`https://apps.sicmy.com/wontodong/`)
- [ ] 지원과 정책: 사용 방법, 문의 방법과 개인정보 처리 내용을 확인하실 수 있습니다. / 버튼: 원투동 지원, 개인정보처리방침

## 7. 원투동 개인정보처리방침·지원 (`apps/wontodong/privacy/`, `apps/wontodong/support/`)

원본: `SG-WonToDong/docs/release/privacy-policy.ko.md`, `support.ko.md` (2026-11-09 17:11 저장본). 본문 문장은 그대로 옮겼고, 의무를 더하거나 빼지 않았습니다. 바꾼 점은 아래뿐입니다.

- [ ] 두 문서 맨 위의 **"작성 메모 (게시 전 삭제)"** 인용 상자와 바로 뒤 구분선을 뺐습니다. 원본이 게시 전에 지우라고 적어 둔 내부 메모입니다.
- [ ] 지원 문서의 `[사이드로드 설치 안내](./sideload-install.ko.md)`는 저장소 안의 파일이라 사이트에 없습니다. **문장은 그대로 두고 링크만 뺐습니다.** 설치 안내를 게시하면 링크를 다시 걸거나, 원본 메모대로 그 내용을 페이지에 넣어 주세요.
- [ ] 제목의 **"(초안)"** 은 원본 그대로 두었습니다. 확정되면 지워 주세요.
- [ ] 원본의 `[오너 확인 …]`, `[확인 필요 …]` 표시는 글자 그대로 두고, 눈에 띄도록 점선 테두리로만 표시했습니다.
- 그 밖에: 제목마다 앵커 id를 붙였고(`#문의하기` 링크 동작), 개인정보처리방침 ↔ 지원 링크는 사이트 경로로 연결했습니다.
- 원본 문서가 다시 바뀌면 이 두 페이지도 다시 옮겨야 합니다.

### 개인정보처리방침에서 정해야 할 것 (원본 표시 그대로)

- [ ] 부칙 시행일: `[오너 확인: YYYY년 MM월 DD일]` (요청대로 자리표시 그대로 둠)
- [ ] 제3조 서버 접속 기록 보유 기간: `[오너 확인: ○일]` (제안: 90일)
- [ ] 제5조 아래: `[오너 확인]` `apps.sicmy.com` 운영 주체가 온노드가 아니면 위탁 표에 추가
- [ ] 제6조 이전받는 자 연락처: `[오너 확인 — Google 개인정보 문의 창구 주소]`
- [ ] 제6조 거부 방법: `[오너 확인: 토글을 두지 않는다면 …로 바꾼다]`
- [ ] 제7조 Android 자동 백업 문장: `[오너 확인 — PRD §10.3-b]`
- [ ] 제13조 전화: `[오너 확인: 대표 전화번호 확정 후 기재]`
- [ ] **(도입 시)** 부분 (Firebase Crashlytics): 한눈에 보기, 제1조, 제2조, 제3조, 제5조, 제6조, 제8조, 제11조. 원본 메모에 따르면 Crashlytics 통합 전에 게시할 때는 이 부분을 빼거나 "도입 예정"으로 바꿔야 합니다.
- [ ] **(제안)** 부분: 제3조 문의 보유 1년, 제6조 오류 보고서 끄기 설정, 제7조 "모든 데이터 지우기" 검토, 제10조 관리 계정 2단계 인증
- [ ] 원본 메모: 법률 검토를 받은 문서가 아님

### 지원 페이지에서 정해야 할 것

- [ ] "여행이 끝나면 어떻게 하나요?": `[확인 필요 — PRD §10.3-a]`
- [ ] "데이터가 백업되나요?": `[확인 필요 — PRD §10.3-b]` 와 이어지는 기울임 글씨의 대체 문장(결정 메모)
- [ ] "사이드로드 설치 안내" 링크 (위 참고)
