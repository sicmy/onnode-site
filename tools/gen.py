# -*- coding: utf-8 -*-
"""One-off generator for the OnNode static site (kept outside the site folder).
The output is plain HTML; nothing here is needed to serve the site."""
import html
import os
import re
import sys
from urllib.parse import quote

SITE = r"D:\dev\Onnode\site"
EMAIL = "oonnode@gmail.com"
BRN = "447-32-01209"
PRETENDARD = "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css"
APK_URL = "https://apps.sicmy.com/wontodong/"

e = html.escape

# ---------------------------------------------------------------- catalog data
# item: (slug, display name, one-line description, select label)
CATALOG = [
    {
        "id": "library", "name": "라이브러리",
        "summary": "Delphi, JavaScript / TypeScript",
        "groups": [
            {"id": "library-delphi", "name": "Delphi", "items": [
                ("hwp-core-library", "HWP Core Library by OnNode",
                 "Delphi에서 한글(HWP) 문서 형식을 다루기 위한 기반 라이브러리",
                 "HWP Core Library by OnNode"),
                ("fastreport-hancom-exports", "FastReport Hancom Exports by OnNode",
                 "FastReport 보고서를 HWP·HWPX 형식으로 저장하는 내보내기 기능 (HWP Core Library 포함)",
                 "FastReport Hancom Exports by OnNode"),
                ("delphi-custom-development", "기능 개발 요청 견적",
                 "필요한 Delphi 기능과 범위를 알려 주시면 개발 견적을 드립니다.",
                 "Delphi 기능 개발 요청"),
            ]},
            {"id": "library-js", "name": "JavaScript / TypeScript", "items": [
                ("beautiful-ui-system", "Beautiful UI System",
                 "웹 화면을 일관된 규칙으로 만들기 위한 UI 디자인 시스템",
                 "Beautiful UI System"),
                ("beautiful-ui-components", "Beautiful UI Components",
                 "shadcn/ui 기반 UI 컴포넌트 모음",
                 "Beautiful UI Components"),
                ("onnode-grid", "OnNode Grid",
                 "웹 애플리케이션용 데이터 그리드 컴포넌트",
                 "OnNode Grid"),
                ("onnode-upload", "OnNode Upload",
                 "웹 애플리케이션용 파일 업로드 컴포넌트",
                 "OnNode Upload"),
            ]},
        ],
    },
    {
        "id": "ieum", "name": "OnNode 이음", "summary": "Alt Text System",
        "groups": [{"items": [
            ("alt-text-system", "Alt Text System",
             "이미지 대체 텍스트(alt text)를 작성하고 관리하기 위한 시스템",
             "OnNode 이음 – Alt Text System"),
        ]}],
    },
    {
        "id": "apm", "name": "APM", "summary": "OnNode Pulse",
        "groups": [{"items": [
            ("onnode-pulse", "OnNode Pulse",
             "애플리케이션 성능 모니터링(APM) 솔루션",
             "OnNode Pulse"),
        ]}],
    },
    {
        "id": "ui-builder", "name": "UI Builder", "summary": "EV IDE (Enterprise Visual IDE)",
        "groups": [{"items": [
            ("ev-ide", "EV IDE (Enterprise Visual IDE)",
             "업무 화면을 시각적으로 구성하는 UI 빌더",
             "EV IDE (Enterprise Visual IDE)"),
        ]}],
    },
    {
        "id": "otp", "name": "OTP", "summary": "OnNode OTP: Simple OTP Library, Enterprise OTP System",
        "groups": [{"id": "onnode-otp", "name": "OnNode OTP", "items": [
            ("onnode-otp-simple", "Simple OTP Library",
             "애플리케이션에 일회용 비밀번호(OTP) 인증을 붙이기 위한 라이브러리",
             "OnNode OTP – Simple OTP Library"),
            ("onnode-otp-enterprise", "Enterprise OTP System",
             "조직 단위로 OTP 인증을 운영하기 위한 시스템",
             "OnNode OTP – Enterprise OTP System"),
        ]}],
    },
    {
        "id": "reporting", "name": "Reporting Tool",
        "summary": "OnNode Report: Viewer, Designer, Data API Server, Reporting Server",
        "groups": [{"id": "onnode-report", "name": "OnNode Report", "items": [
            ("onnode-report-viewer", "Viewer",
             "보고서를 화면에서 보고 출력하는 뷰어",
             "OnNode Report – Viewer"),
            ("onnode-report-designer", "Designer",
             "보고서 양식을 만드는 디자이너",
             "OnNode Report – Designer"),
            ("onnode-report-data-api", "Data API Server (API)",
             "보고서에 쓸 데이터를 API로 제공하는 서버",
             "OnNode Report – Data API Server (API)"),
            ("onnode-report-server", "Reporting Server (Web, JavaScript, Java)",
             "Web·JavaScript·Java 환경에서 보고서를 생성해 제공하는 서버",
             "OnNode Report – Reporting Server (Web, JavaScript, Java)"),
        ]}],
    },
    {
        "id": "server-access", "name": "서버접근제어", "summary": "OnNode Gate",
        "groups": [{"items": [
            ("onnode-gate", "OnNode Gate",
             "서버 접근을 통제하기 위한 서버접근제어 솔루션",
             "OnNode Gate"),
        ]}],
    },
    {
        "id": "open-source", "name": "오픈소스·협업 솔루션 구축/지원",
        "summary": "GitLab, Jira / Confluence / Bitbucket, Mattermost, Warpgate, Kubernetes, Proxmox, RustDesk, Redis / Kafka",
        "note": "아래 오픈소스와 협업 도구의 설치·구성과 운영 지원을 제공합니다.",
        "groups": [{"items": [
            ("gitlab", "GitLab", "소스 코드 저장소와 CI/CD 플랫폼", "GitLab 구축/지원"),
            ("jira-confluence-bitbucket", "Jira / Confluence / Bitbucket",
             "이슈 관리, 문서 협업, 코드 저장소 도구", "Jira / Confluence / Bitbucket 구축/지원"),
            ("mattermost", "Mattermost", "팀 메신저", "Mattermost 구축/지원"),
            ("warpgate", "Warpgate", "서버 접속을 중계하는 배스천(bastion) 호스트", "Warpgate 구축/지원"),
            ("kubernetes", "Kubernetes", "컨테이너 오케스트레이션 플랫폼", "Kubernetes 구축/지원"),
            ("proxmox", "Proxmox", "서버 가상화 플랫폼", "Proxmox 구축/지원"),
            ("rustdesk", "RustDesk", "원격 데스크톱 도구", "RustDesk 구축/지원"),
            ("redis-kafka", "Redis / Kafka", "인메모리 데이터 저장소와 메시지 스트리밍 플랫폼", "Redis / Kafka 구축/지원"),
        ]}],
    },
    {
        "id": "tech-support", "name": "기술지원",
        "summary": "오픈소스 기술지원 서비스팩, 오픈소스를 이용한 시스템 구축",
        "groups": [{"items": [
            ("support-pack-1m", "오픈소스 기술지원 서비스팩 (1개월)",
             "1개월 단위 오픈소스 기술지원",
             "오픈소스 기술지원 서비스팩 (1개월)"),
            ("support-pack-1y", "오픈소스 기술지원 서비스팩 (1년)",
             "1년 단위 오픈소스 기술지원",
             "오픈소스 기술지원 서비스팩 (1년)"),
            ("open-source-system-build", "오픈소스를 이용한 시스템 구축",
             "구축 범위와 요구 사항을 알려 주시면 견적을 드립니다.",
             "오픈소스를 이용한 시스템 구축"),
        ]}],
    },
]

ALL_SLUGS = [it[0] for c in CATALOG for g in c["groups"] for it in g["items"]]
assert len(ALL_SLUGS) == len(set(ALL_SLUGS)), "duplicate slug"

# ---------------------------------------------------------------- shell
def head(prefix, title, description):
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#121417" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="온노드 OnNode">
<meta property="og:locale" content="ko_KR">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="{PRETENDARD}">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
"""


def header(prefix, current):
    home = prefix or "./"

    def item(href, label, key, extra=""):
        cur = ' aria-current="page"' if key == current else ""
        cls = f' class="{extra}"' if extra else ""
        return f'<li><a href="{href}"{cls}{cur}>{label}</a></li>'

    return f"""<a class="skip-link" href="#main">본문 바로가기</a>
<header class="site-header">
  <div class="container">
    <a class="wordmark" href="{home}"><span class="wordmark-dot" aria-hidden="true"></span>OnNode<span class="sr-only"> 홈</span></a>
    <nav class="site-nav" aria-label="주 메뉴">
      <ul>
        {item(prefix + "solutions/", "솔루션", "solutions")}
        {item(prefix + "apps/wontodong/", "앱", "apps")}
        {item(prefix + "quote/", "견적 요청", "quote", "nav-quote")}
      </ul>
    </nav>
  </div>
</header>
"""


def footer(prefix):
    home = prefix or "./"
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <a class="wordmark" href="{home}"><span class="wordmark-dot" aria-hidden="true"></span>OnNode<span class="sr-only"> 홈</span></a>
      <nav class="footer-nav" aria-label="하단 메뉴">
        <ul>
          <li><a href="{prefix}solutions/">솔루션</a></li>
          <li><a href="{prefix}quote/">견적 요청</a></li>
          <li><a href="{prefix}apps/wontodong/">원투동</a></li>
          <li><a href="{prefix}apps/wontodong/support/">원투동 지원</a></li>
          <li><a href="{prefix}apps/wontodong/privacy/">원투동 개인정보처리방침</a></li>
        </ul>
      </nav>
    </div>
    <h2 class="sr-only">사업자 정보</h2>
    <dl class="biz">
      <div><dt>회사명</dt><dd>온노드 (OnNode)</dd></div>
      <div><dt>대표</dt><dd>오해란</dd></div>
      <div><dt>사업자등록번호</dt><dd class="num">{BRN}</dd></div>
      <div><dt>주소</dt><dd>서울특별시 서대문구 북아현로 90-7, 2층(북아현동)</dd></div>
      <div><dt>전화</dt><dd class="num">000-0000-0000</dd></div>
      <div><dt>이메일</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div><dt>업태</dt><dd>도매 및 소매업, 임대서비스업</dd></div>
      <div><dt>종목</dt><dd>컴퓨터 및 주변장치, 소프트웨어 도매업</dd></div>
    </dl>
    <p class="copyright"><small>&copy; 2026 OnNode.</small></p>
  </div>
</footer>
"""


def page(path, prefix, current, title, description, body, body_class="", tail=""):
    cls = f' class="{body_class}"' if body_class else ""
    doc = (head(prefix, title, description)
           + f"<body{cls}>\n"
           + header(prefix, current)
           + f'<main id="main" tabindex="-1">\n{body}</main>\n'
           + footer(prefix)
           + tail
           + "</body>\n</html>\n")
    out = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(doc)
    print("wrote", path)


# ---------------------------------------------------------------- mailto
FIELDS = ["요청자", "회사", "전화번호", "이메일", "항목", "내용"]


def mailto(item_label=""):
    subject = "[견적 요청]" + (f" {item_label}" if item_label else "")
    lines = [f"{f}: " + (item_label if f == "항목" else "") for f in FIELDS]
    body = "\r\n".join(lines) + "\r\n"
    return f"mailto:{EMAIL}?subject={quote(subject, safe='')}&body={quote(body, safe='')}"


# ---------------------------------------------------------------- pages
def build_index():
    tiles = []
    for c in CATALOG:
        tiles.append(f"""        <li class="tile">
          <h3><span class="led" aria-hidden="true"></span><a href="solutions/#{c['id']}">{e(c['name'])}</a></h3>
          <p>{e(c['summary'])}</p>
        </li>""")
    body = f"""<section class="hero" aria-labelledby="hero-title">
  <div class="container">
    <h1 id="hero-title">소프트웨어 라이브러리와 솔루션을 공급하고, 오픈소스 시스템을 구축합니다</h1>
    <p class="lead">온노드는 업무용 소프트웨어 개발에 쓰는 라이브러리와 솔루션을 공급하고, 오픈소스를 이용한 시스템 구축과 기술지원을 합니다. 필요한 항목과 범위를 알려 주시면 확인한 뒤 견적을 보내 드립니다.</p>
    <div class="actions">
      <a class="btn btn-primary" href="quote/">견적 요청</a>
      <a class="btn btn-secondary" href="solutions/">솔루션 보기</a>
    </div>
  </div>
</section>

<section class="band" aria-labelledby="solutions-title">
  <div class="container">
    <div class="section-head">
      <h2 id="solutions-title">솔루션</h2>
      <a href="solutions/">전체 목록 보기</a>
    </div>
    <ul class="tiles">
{chr(10).join(tiles)}
    </ul>
  </div>
</section>

<section class="band" aria-labelledby="apps-title">
  <div class="container">
    <div class="section-head">
      <h2 id="apps-title">앱</h2>
    </div>
    <div class="app-row">
      <div>
        <h3>원투동 – 베트남 돈 계산기</h3>
        <p>베트남 여행 중 현금으로 낼 돈과 거스름돈을 계산하고, 환율을 확인하고, 쓴 현금을 기록하는 앱입니다. 온노드가 만들고 배포합니다.</p>
      </div>
      <div class="actions">
        <a class="btn btn-secondary" href="apps/wontodong/">앱 소개</a>
        <a class="btn btn-secondary" href="apps/wontodong/support/">원투동 지원</a>
      </div>
    </div>
  </div>
</section>

<section class="band cta-band" aria-labelledby="cta-title">
  <div class="container">
    <div>
      <h2 id="cta-title">견적 요청</h2>
      <p>제품 공급, 기능 개발, 시스템 구축과 기술지원 견적은 이메일로 받고 있습니다.</p>
    </div>
    <div class="actions">
      <a class="btn btn-primary" href="quote/">견적 요청하기</a>
    </div>
  </div>
</section>
"""
    page("index.html", "", "home",
         "온노드 OnNode | 소프트웨어 라이브러리·솔루션 공급, 오픈소스 구축·기술지원",
         "온노드(OnNode)는 소프트웨어 라이브러리와 솔루션을 공급하고, 오픈소스를 이용한 시스템 구축과 기술지원을 합니다.",
         body, body_class="home")


def build_solutions():
    nav = "\n".join(
        f'          <li><a href="#{c["id"]}">{e(c["name"])}</a></li>' for c in CATALOG)
    sections = []
    for c in CATALOG:
        parts = [f'  <section class="category" id="{c["id"]}" aria-labelledby="{c["id"]}-title">',
                 f'    <h2 id="{c["id"]}-title"><span class="led" aria-hidden="true"></span>{e(c["name"])}</h2>']
        if c.get("note"):
            parts.append(f'    <p class="category-note">{e(c["note"])}</p>')
        for g in c["groups"]:
            gid = f' id="{g["id"]}"' if g.get("id") else ""
            parts.append(f'    <div class="group"{gid}>')
            if g.get("name"):
                parts.append(f'      <h3>{e(g["name"])}</h3>')
            parts.append('      <ul class="products">')
            for slug, name, desc, label in g["items"]:
                parts.append(f"""        <li class="product">
          <div>
            <p class="product-name">{e(name)}</p>
            <p class="product-desc">{e(desc)}</p>
          </div>
          <a class="btn btn-secondary btn-small" href="../quote/?item={slug}">견적 요청<span class="sr-only">: {e(label)}</span></a>
        </li>""")
            parts.append('      </ul>')
            parts.append('    </div>')
        parts.append('  </section>')
        sections.append("\n".join(parts))
    body = f"""<div class="container">
  <header class="page-head">
    <h1>솔루션</h1>
    <p class="lead">온노드가 공급하는 라이브러리와 솔루션, 구축과 기술지원 서비스입니다. 항목마다 견적을 요청할 수 있습니다.</p>
  </header>
  <div class="catalog">
    <nav class="catalog-nav" aria-labelledby="catalog-nav-title">
      <div>
        <h2 id="catalog-nav-title">분류</h2>
        <ul>
{nav}
        </ul>
      </div>
    </nav>
    <div>
{chr(10).join(sections)}
      <p class="fineprint">Delphi, FastReport, 한글(HWP), shadcn/ui, GitLab, Jira, Confluence, Bitbucket, Mattermost, Warpgate, Kubernetes, Proxmox, RustDesk, Redis, Kafka, Java, JavaScript 등 제3자 제품명은 각 권리자의 상표이며, 제품을 구분하기 위해서만 표기했습니다.</p>
    </div>
  </div>
</div>
"""
    page("solutions/index.html", "../", "solutions",
         "솔루션 | 온노드 OnNode",
         "온노드의 라이브러리(Delphi, JavaScript/TypeScript), APM, OTP, 리포팅, 서버접근제어, 오픈소스·협업 솔루션 구축/지원과 기술지원 목록입니다.",
         body)


QUOTE_JS = """<script>
(function () {
  var slug = new URLSearchParams(window.location.search).get("item");
  if (!slug) return;
  var select = document.getElementById("q-item");
  var option = null;
  for (var i = 0; i < select.options.length; i++) {
    if (select.options[i].value === slug) { option = select.options[i]; break; }
  }
  if (!option || !option.value) return;
  select.value = option.value;
  var label = option.textContent;
  var shown = document.getElementById("selected-item");
  shown.querySelector("strong").textContent = label;
  shown.hidden = false;
  var lines = ["요청자: ", "회사: ", "전화번호: ", "이메일: ", "항목: " + label, "내용: "];
  document.getElementById("mail-link").href = "mailto:%(email)s?subject=" +
    encodeURIComponent("[견적 요청] " + label) + "&body=" + encodeURIComponent(lines.join("\\r\\n") + "\\r\\n");
})();
</script>
""" % {"email": EMAIL}


def build_quote():
    groups = []
    for c in CATALOG:
        opts = "\n".join(
            f'                <option value="{slug}">{e(label)}</option>'
            for g in c["groups"] for slug, _n, _d, label in g["items"])
        groups.append(f'              <optgroup label="{e(c["name"])}">\n{opts}\n              </optgroup>')
    field_items = "\n".join(f"          <li>{f}</li>" for f in FIELDS)
    body = f"""<div class="container">
  <header class="page-head">
    <h1>견적 요청</h1>
    <p class="lead">제품 공급, 기능 개발, 시스템 구축과 기술지원 견적을 요청하실 수 있습니다.</p>
  </header>
  <div class="quote-layout">
    <section class="notice" aria-labelledby="notice-title">
      <h2 class="notice-title" id="notice-title"><span class="led" aria-hidden="true"></span>온라인 접수는 준비 중입니다. 아래 항목을 이메일로 보내 주세요.</h2>
      <p class="selected-item" id="selected-item" hidden>선택한 항목: <strong></strong></p>
      <a class="btn btn-primary" id="mail-link" href="{e(mailto())}">이메일로 견적 요청</a>
      <div class="notice-detail">
        <p>받는 주소: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p>메일 제목: [견적 요청]</p>
        <p>버튼을 눌러도 메일 앱이 열리지 않으면 위 주소로 직접 보내 주세요.</p>
      </div>
      <div class="mail-template">
        <p>메일에 적어 주실 항목</p>
        <ul>
{field_items}
        </ul>
      </div>
    </section>

    <form class="quote-form" aria-describedby="form-hint" novalidate>
      <fieldset class="form-preview" disabled>
        <legend>온라인 견적 요청 양식 (준비 중)</legend>
        <p class="form-hint" id="form-hint">이 양식은 아직 접수되지 않습니다. 같은 내용을 이메일로 보내 주세요.</p>
        <div class="form-grid">
          <div class="field">
            <label for="q-name">요청자</label>
            <input id="q-name" name="name" type="text" autocomplete="name">
          </div>
          <div class="field">
            <label for="q-company">회사</label>
            <input id="q-company" name="company" type="text" autocomplete="organization">
          </div>
          <div class="field">
            <label for="q-phone">전화번호</label>
            <input id="q-phone" name="phone" type="tel" autocomplete="tel">
          </div>
          <div class="field">
            <label for="q-email">이메일</label>
            <input id="q-email" name="email" type="email" autocomplete="email">
          </div>
          <div class="field field-full">
            <label for="q-item">항목</label>
            <select id="q-item" name="item">
              <option value="">항목을 선택하세요</option>
{chr(10).join(groups)}
              <option value="other">기타 / 아직 정하지 않음</option>
            </select>
          </div>
          <div class="field field-full">
            <label for="q-message">내용</label>
            <textarea id="q-message" name="message" rows="6"></textarea>
          </div>
        </div>
        <div class="actions">
          <button class="btn" type="submit">온라인 접수 준비 중</button>
        </div>
      </fieldset>
    </form>
  </div>
</div>
"""
    page("quote/index.html", "../", "quote",
         "견적 요청 | 온노드 OnNode",
         "온노드 제품 공급, 기능 개발, 시스템 구축과 기술지원 견적을 이메일로 요청하실 수 있습니다.",
         body, tail=QUOTE_JS)


def build_app():
    features = [
        ("현금 지불·거스름돈 계산", "계산대 앞에서 낼 지폐와 받을 거스름돈을 계산합니다."),
        ("환율", "원화(KRW)와 베트남 동(VND) 금액을 환율로 바꿔 계산합니다."),
        ("현금 가계부", "여행 중 현금으로 쓴 돈을 일자별로 기록합니다."),
        ("오프라인 우선", "마지막으로 받은 환율과 기기에 저장한 기록으로, 인터넷 연결 없이도 계산과 기록을 할 수 있습니다."),
        ("광고·회원가입 없음", "광고가 없고, 가입 없이 바로 씁니다."),
    ]
    items = "\n".join(
        f'        <div>\n          <dt><span class="led" aria-hidden="true"></span>{e(t)}</dt>\n          <dd>{e(d)}</dd>\n        </div>'
        for t, d in features)
    body = f"""<div class="container">
  <header class="page-head">
    <h1>원투동 – 베트남 돈 계산기</h1>
    <p class="lead">베트남 여행 중 현금으로 낼 돈과 거스름돈을 계산하고, 환율을 확인하고, 쓴 현금을 기록하는 앱입니다.</p>
  </header>

  <section class="app-section" aria-labelledby="features-title">
    <h2 id="features-title">주요 기능</h2>
    <dl class="feature-list">
{items}
    </dl>
  </section>

  <section class="app-section" aria-labelledby="download-title">
    <h2 id="download-title">내려받기</h2>
    <p>Android 테스트 버전은 <a href="{APK_URL}">apps.sicmy.com/wontodong</a>에서 배포하고 있습니다. 앱 스토어 출시는 이후에 안내합니다.</p>
    <div class="actions">
      <a class="btn btn-primary" href="{APK_URL}">Android 테스트 버전 받기</a>
    </div>
  </section>

  <section class="app-section" aria-labelledby="help-title">
    <h2 id="help-title">지원과 정책</h2>
    <p>사용 방법, 문의 방법과 개인정보 처리 내용을 확인하실 수 있습니다.</p>
    <div class="actions">
      <a class="btn btn-secondary" href="support/">원투동 지원</a>
      <a class="btn btn-secondary" href="privacy/">개인정보처리방침</a>
    </div>
  </section>
</div>
"""
    page("apps/wontodong/index.html", "../../", "apps",
         "원투동 – 베트남 돈 계산기 | 온노드 OnNode",
         "원투동은 베트남 여행 중 현금 지불과 거스름돈 계산, 환율 확인, 현금 가계부 기록을 돕는 앱입니다. 오프라인 우선, 광고·회원가입 없음.",
         body)


# ---------------------------------------------------------------- markdown (subset)
INLINE_CODE = re.compile(r"`([^`]+)`")


def inline(text, prefix_links=None):
    """Escape and render a markdown inline subset: code, links, bold, italic, autolinks."""
    stash = []

    def keep(s):
        stash.append(s)
        return f"\x00{len(stash) - 1}\x00"

    text = INLINE_CODE.sub(lambda m: keep(f"<code>{e(m.group(1))}</code>"), text)

    def link(m):
        label, href = m.group(1), m.group(2).strip()
        if prefix_links:
            href = prefix_links(href)
        if href is None:  # target not published on the site: keep the words, drop the link
            return keep(inline(label))
        return keep(f'<a href="{e(href, quote=True)}">{inline(label)}</a>')

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", link, text)
    text = re.sub(r"<(https?://[^>\s]+)>", lambda m: keep(f'<a href="{e(m.group(1))}">{e(m.group(1))}</a>'), text)
    text = re.sub(r"<([^>\s@]+@[^>\s]+)>", lambda m: keep(f'<a href="mailto:{e(m.group(1))}">{e(m.group(1))}</a>'), text)
    text = e(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    # bare URLs and emails not already linked (ASCII only, so trailing Hangul
    # particles such as "으로" / "에서" stay outside the link)
    def bare_url(m):
        url = m.group(1)
        trail = ""
        while url and url[-1] in ".,;:!?'":
            trail = url[-1] + trail
            url = url[:-1]
        return keep(f'<a href="{url}">{url}</a>') + trail

    text = re.sub(r"(?<![\"=/A-Za-z0-9])(https?://[A-Za-z0-9._~:/?#@!$&'*+,;=%-]+)", bare_url, text)
    text = re.sub(r"(?<![A-Za-z0-9._%+:/\"-])([A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+)",
                  lambda m: keep(f'<a href="mailto:{m.group(1)}">{m.group(1)}</a>'), text)
    # Unresolved owner decisions in the source drafts: same words, highlighted.
    text = re.sub(r"\[(?:오너 확인|확인 필요)[^\]]*\]", lambda m: f'<mark class="todo">{m.group(0)}</mark>', text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)
    return text


def md_to_html(md, shift=0, skip_h1=True, prefix_links=None):
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    i = 0
    title = None
    para = []

    used_ids = set()

    def heading_id(raw):
        plain = re.sub(r"[`*_\[\]()]", "", raw)
        hid = re.sub(r"[^\w-]+", "-", plain).strip("-").lower() or "section"
        base, n = hid, 2
        while hid in used_ids:
            hid = f"{base}-{n}"; n += 1
        used_ids.add(hid)
        return hid

    def flush_para():
        if para:
            out.append("<p>" + "\n".join(inline(p.strip(), prefix_links) for p in para) + "</p>")
            para.clear()

    def is_block_start(s):
        return bool(re.match(r"^(#{1,6}\s|[-*+]\s|\d+[.)]\s|>|\||---+\s*$|\*\*\*+\s*$|```)", s.strip()))

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            flush_para(); i += 1; continue
        if s.startswith("<!--"):
            flush_para()
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", s)
        if m:
            flush_para()
            level = len(m.group(1))
            if level == 1 and title is None:
                title = m.group(2)
                if skip_h1:
                    i += 1; continue
            lv = min(6, max(2, level + shift))
            out.append(f'<h{lv} id="{e(heading_id(m.group(2)))}">{inline(m.group(2), prefix_links)}</h{lv}>')
            i += 1; continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            flush_para(); out.append("<hr>"); i += 1; continue
        if s.startswith("```"):
            flush_para()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + e("\n".join(buf)) + "</code></pre>")
            continue
        if s.startswith(">"):
            flush_para()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>\n" + md_to_html("\n".join(buf), shift, False, prefix_links)[0] + "\n</blockquote>")
            continue
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            flush_para()
            def cells(row):
                row = row.strip().strip("|")
                return [c.strip() for c in row.split("|")]
            hdr = cells(lines[i]); i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            t = ['<div class="table-wrap"><table>', "<thead><tr>" + "".join(f'<th scope="col">{inline(c, prefix_links)}</th>' for c in hdr) + "</tr></thead>", "<tbody>"]
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c, prefix_links)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table></div>")
            out.append("\n".join(t))
            continue
        lm = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if lm:
            flush_para()
            html_list, i = parse_list(lines, i, prefix_links)
            out.append(html_list)
            continue
        para.append(line)
        i += 1
    flush_para()
    return "\n".join(out), title


def parse_list(lines, i, prefix_links):
    first = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
    base = len(first.group(1).expandtabs(4))
    ordered = first.group(2)[0].isdigit()
    tag = "ol" if ordered else "ul"
    start = ""
    if ordered:
        n = int(re.match(r"\d+", first.group(2)).group(0))
        if n != 1:
            start = f' start="{n}"'
    items = []
    while i < len(lines):
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", lines[i])
        if not m:
            # continuation line of previous item (indented, non-empty)
            if lines[i].strip() and items and (len(lines[i]) - len(lines[i].lstrip())) > base:
                items[-1]["text"] += " " + lines[i].strip(); i += 1; continue
            break
        ind = len(m.group(1).expandtabs(4))
        if ind < base:
            break
        if ind > base:
            sub, i = parse_list(lines, i, prefix_links)
            items[-1]["sub"].append(sub)
            continue
        if m.group(2)[0].isdigit() != ordered:
            break
        items.append({"text": m.group(3), "sub": []})
        i += 1
    body = []
    for it in items:
        txt = it["text"]
        cb = re.match(r"^\[( |x|X)\]\s+(.*)$", txt)
        if cb:
            txt = ("☑ " if cb.group(1).lower() == "x" else "☐ ") + cb.group(2)
        body.append("<li>" + inline(txt, prefix_links) + "".join("\n" + s for s in it["sub"]) + "</li>")
    return f"<{tag}{start}>\n" + "\n".join(body) + f"\n</{tag}>", i


SRC_DIR = r"D:\dev\SGSoft\mobile apps\SG-WonToDong\docs\release"


def build_policy_page(kind):
    if kind == "privacy":
        src = os.path.join(SRC_DIR, "privacy-policy.ko.md")
        crumb, default_title = "개인정보처리방침", "원투동 개인정보처리방침"
        desc = "원투동 – 베트남 돈 계산기 앱의 개인정보처리방침입니다."
    else:
        src = os.path.join(SRC_DIR, "support.ko.md")
        crumb, default_title = "지원", "원투동 지원"
        desc = "원투동 – 베트남 돈 계산기 앱의 사용 안내와 문의 방법입니다."
    if os.path.exists(src):
        with open(src, encoding="utf-8") as f:
            md = f.read().replace("\r\n", "\n")

        # Drop the drafting memo the source marks "게시 전 삭제" (and the rule after it).
        md, n_memo = re.subn(r"\n>\s*\*\*작성 메모 \(게시 전 삭제\)\*\*.*?(?:\n>.*?)*\n(?:\s*\n)*(?:---\s*\n)?",
                             "\n", md, count=1)
        print(f"  {kind}: drafting memo removed = {bool(n_memo)}")

        def fix_links(href):
            # Map links between the release docs onto the site pages.
            if href.endswith("privacy-policy.ko.md"):
                return "../privacy/"
            if href.endswith("support.ko.md"):
                return "../support/"
            if href.endswith(".md"):
                return None  # repo-only document, not on the site
            return href

        content, title = md_to_html(md, shift=0, skip_h1=True, prefix_links=fix_links)
        title_text = re.sub(r"[*`]", "", title) if title else default_title
        content = "\n".join("    " + l if l else l for l in content.split("\n"))
    else:
        title_text = default_title
        content = f"""    <div class="placeholder">
      <p><strong>준비 중입니다.</strong> {crumb} 내용을 정리하고 있습니다. 문의는 <a href="mailto:{EMAIL}">{EMAIL}</a>로 보내 주세요.</p>
    </div>"""
    body = f"""<div class="container">
  <header class="page-head">
    <nav class="crumbs" aria-label="이동 경로">
      <ol>
        <li><a href="../">원투동</a></li>
        <li aria-current="page">{crumb}</li>
      </ol>
    </nav>
    <h1>{e(title_text)}</h1>
  </header>
  <div class="prose">
{content}
  </div>
</div>
"""
    page(f"apps/wontodong/{kind}/index.html", "../../../", "apps",
         f"{title_text} | 온노드 OnNode", desc, body)
    return os.path.exists(src)


if __name__ == "__main__":
    what = sys.argv[1:] or ["main"]
    if "main" in what:
        build_index(); build_solutions(); build_quote(); build_app()
    if "policy" in what:
        print("privacy source:", build_policy_page("privacy"))
        print("support source:", build_policy_page("support"))
