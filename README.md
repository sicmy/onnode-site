# 온노드 (OnNode) 회사 웹사이트

온노드(OnNode)의 정적 회사 소개 사이트입니다. 빌드 과정 없이 HTML 파일과 CSS 파일 하나로 되어 있으며, GitHub Pages에 그대로 올려 서비스합니다.

- 주소: `https://www.onnode.co.kr/` (2026-11-09 연결, `onnode.co.kr`은 www로 자동 이동)
- DNS: 호스팅케이알 — `@` A 185.199.108–111.153, `www` CNAME `sicmy.github.io`, 도메인 인증 TXT `_github-pages-challenge-sicmy`
- `CNAME` 파일은 GitHub Pages 설정이 관리한다. 지우지 말 것. 예전 주소 `https://sicmy.github.io/onnode-site/`는 새 주소로 이동한다

두 주소에서 모두 동작하도록 **모든 내부 링크와 파일 경로는 상대 경로**로 작성했습니다. 새 페이지를 추가할 때도 `/`로 시작하는 절대 경로를 쓰지 마세요.

## 구조

```
site/
├── index.html                       회사 소개, 솔루션 분류, 원투동 앱, 견적 요청 안내
├── solutions/index.html             전체 제품·서비스 목록 (분류별 앵커: #library, #otp 등)
├── quote/index.html                 견적 요청 (정적 양식 미리보기 + 이메일 접수)
├── apps/wontodong/index.html        원투동 앱 소개
├── apps/wontodong/privacy/index.html  원투동 개인정보처리방침
├── apps/wontodong/support/index.html  원투동 지원
├── assets/style.css                 전체 스타일 (색상 토큰, 다크 모드 포함)
├── assets/favicon.svg               파비콘
├── .nojekyll                        GitHub Pages의 Jekyll 처리 끄기
├── README.md                        이 문서
└── REVIEW.md                        게시 전 검토 목록
```

- 글꼴: Pretendard Variable (jsDelivr CDN), 불러오지 못하면 시스템 글꼴로 표시합니다.
- 자바스크립트: `quote/index.html` 끝의 짧은 스크립트 하나뿐입니다. 솔루션 페이지에서 `견적 요청`을 누르면 `?item=<slug>` 값으로 항목을 미리 고르고 메일 제목·본문에 항목 이름을 넣습니다. 스크립트가 없어도 메일 버튼은 동작합니다.
- 머리글(헤더)과 바닥글(사업자 정보)은 각 HTML 파일에 그대로 들어 있습니다. 사업자 정보를 바꿀 때는 모든 `index.html`에서 같은 부분을 함께 고쳐 주세요.
- 제품 목록을 바꿀 때는 `solutions/index.html`의 항목과 `quote/index.html`의 `<select id="q-item">` 선택지를 함께 고쳐 주세요. 두 파일의 `item` 값(slug)이 같아야 항목이 미리 선택됩니다.

## 로컬에서 미리 보기

```bash
cd site
python -m http.server 8000
```

브라우저에서 `http://localhost:8000/` 을 엽니다. 폴더 링크(`solutions/` 등)가 `index.html`로 열리려면 파일을 직접 여는 대신 이렇게 서버로 띄워야 합니다.

## GitHub Pages 배포

1. GitHub에 `onnode-site` 저장소를 만들고 이 폴더 내용을 `main` 브랜치에 올립니다.
2. 저장소 **Settings → Pages**에서 Source를 `Deploy from a branch`, Branch를 `main` / `/ (root)`로 지정합니다.
3. 몇 분 뒤 `https://sicmy.github.io/onnode-site/` 에서 확인합니다.

`.nojekyll` 파일이 있으므로 Jekyll 변환 없이 파일이 그대로 서비스됩니다.

## 나중에 도메인 바꾸기 (www.onnode.co.kr)

**DNS를 먼저 바꾼 뒤에** 진행하세요. 순서가 바뀌면 사이트가 잠시 열리지 않을 수 있습니다.

1. 도메인 DNS에 `www` CNAME 레코드를 `sicmy.github.io.` 로 추가합니다.
2. DNS가 반영된 것을 확인한 뒤, 이 폴더 루트에 `CNAME` 파일을 만들고 한 줄로 `www.onnode.co.kr` 을 적어 커밋·푸시합니다. (또는 Settings → Pages → Custom domain에 입력해도 같은 파일이 만들어집니다.)
3. Settings → Pages에서 **Enforce HTTPS**를 켭니다.
4. 필요하면 `onnode.co.kr`(www 없는 주소)도 GitHub Pages IP로 A 레코드를 연결합니다.

내부 링크가 모두 상대 경로이므로 HTML은 고칠 필요가 없습니다. 도메인이 정해진 뒤에는 각 페이지 `<head>`에 `og:url`, `link rel="canonical"`, 공유용 `og:image`(절대 주소)를 추가하면 좋습니다. 지금은 주소가 바뀔 예정이라 넣지 않았습니다.

## TODO

- [ ] 실제 대표 전화번호로 바꾸기 (현재 모든 페이지 바닥글에 `000-0000-0000`)
- [ ] 견적 요청 온라인 접수 기능 (양식 전송 백엔드). 지금은 양식이 비활성 상태이고 이메일로만 받습니다.
- [ ] `REVIEW.md`의 문구 검토
- [ ] 원투동 개인정보처리방침·지원 페이지의 미확정 항목 정리: 시행일(원본의 `[오너 확인: YYYY년 MM월 DD일]`을 그대로 옮겨 둠), 점선으로 표시된 `[오너 확인]`·`[확인 필요]` 자리, `(도입 시)`·`(제안)` 부분, 제목의 `(초안)`. 자세한 목록은 `REVIEW.md` 7번.
- [ ] 원투동 지원 페이지의 "사이드로드 설치 안내" 연결 (설치 안내 문서를 게시한 뒤 링크 추가)
- [ ] 도메인 연결 후 `CNAME`, `og:url`, `canonical`, `og:image` 추가
