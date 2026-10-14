"""Generate the four MT Auto Care pages with shared head, header and footer."""
import sys, os

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def u(pid, w=1400):
    return f"https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&q=82"

HERO = 'photo-1503376780353-7e6692767b70'
RED = 'photo-1552519507-da3b142c6e3d'
DETAIL = 'photo-1507136566006-cfc505b114fc'
WASH = 'photo-1492144534655-ae79c964c9d7'
INTERIOR = 'photo-1489824904134-891ab64532f1'
PORSCHE = 'photo-1544636331-e26879cd4d9b'
MUSTANG = 'photo-1494976388531-d1058494cdd8'
ORANGE = 'photo-1583121274602-3e2820c69888'

def img(pid, w, alt, extra='', fallback=None):
    fb = f' data-fallback="{u(fallback, w)}"' if fallback else ''
    return f'<img loading="lazy" src="{u(pid, w)}" alt="{alt}"{fb}{extra}>'

PHONE = '0823418418'
PHONE_TXT = '0823 418 418'
EMAIL = 'lienhe@mtautocare.com'
# public address of the site; change to https://mtautocare.com/ once the domain points here
SITE_URL = 'https://mtautocare.com/'
ADDRESS = '71A Tôn Thất Tùng, Phường Pleiku, tỉnh Gia Lai'
ADDRESS_OLD = 'trước đây: P. Phù Đổng, TP. Pleiku'
MAP_Q = '71A+T%C3%B4n+Th%E1%BA%A5t+T%C3%B9ng,+Pleiku,+Gia+Lai'
LAT, LNG = '13.976097447147358', '108.02574437143453'  # MT Auto's pin, as provided by the shop
MAP_EMBED = f'https://maps.google.com/maps?q={LAT},{LNG}&z=17&hl=vi&output=embed'
# the shop's own Google Maps pin (opens the exact place, with name and reviews)
MAP_DIR = 'https://maps.app.goo.gl/7KgHm1zZEK48gmLy6'
FB = 'https://www.facebook.com/mt.autochamsocxe'
MSG = 'https://m.me/mt.autochamsocxe'
ZALO = f'https://zalo.me/{PHONE}'

ICON_PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
ICON_MSG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.36 2 2 6.13 2 11.7c0 2.91 1.19 5.44 3.14 7.17.16.14.26.35.27.57l.05 1.78a.8.8 0 0 0 1.12.71l1.98-.87a.8.8 0 0 1 .53-.04c.91.25 1.88.38 2.91.38 5.64 0 10-4.13 10-9.7S17.64 2 12 2zm6 7.46-2.94 4.66a1.5 1.5 0 0 1-2.17.4l-2.34-1.75a.6.6 0 0 0-.72 0l-3.16 2.4c-.42.32-.97-.18-.69-.63l2.94-4.66a1.5 1.5 0 0 1 2.17-.4l2.34 1.75a.6.6 0 0 0 .72 0l3.16-2.4c.42-.32.97.18.69.63z"/></svg>'

PAGES = [
    ('index.html', 'Trang chủ'),
    ('dich-vu.html', 'Dịch vụ'),
    ('cong-trinh.html', 'Công trình'),
    ('lien-he.html', 'Liên hệ'),
]

def head(title, desc, fname):
    url = SITE_URL + ('' if fname == 'index.html' else fname)
    return f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#0e0e0d">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="MT Auto Care">
<meta property="og:locale" content="vi_VN">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_URL}assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="MT Auto Care — Chăm chút từng chi tiết">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE_URL}assets/og.jpg">
<link rel="icon" href="assets/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap&subset=vietnamese" rel="stylesheet">
<script>document.documentElement.classList.add('js');try{{if(sessionStorage.getItem('mt-pt')==='1')document.documentElement.classList.add('pt-arrive')}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"AutoRepair","name":"MT Auto Care","image":"{SITE_URL}assets/og.jpg","url":"{SITE_URL}","telephone":"+84823418418","email":"{EMAIL}","address":{{"@type":"PostalAddress","streetAddress":"71A Tôn Thất Tùng","addressLocality":"Phường Pleiku","addressRegion":"Gia Lai","addressCountry":"VN"}},"geo":{{"@type":"GeoCoordinates","latitude":{LAT},"longitude":{LNG}}},"hasMap":"{MAP_DIR}","sameAs":["{FB}"]}}</script>
<noscript><style>
.loader,.cursor,.pt{{display:none!important}}
body.is-loading{{overflow:auto!important}}
.header-intro,.hero-up,.fab,.totop{{opacity:1!important;transform:none!important}}
.hero-img img{{transform:none!important}}
.intro-text .w{{color:inherit!important}}
.zoom{{height:auto!important}}.zoom-stick{{position:relative!important}}.zoom-img{{clip-path:none!important}}.zoom-words{{display:none}}.zoom-cap{{opacity:1!important;transform:none!important}}
.pstep{{opacity:1!important}}
.foot-mark span{{transform:none!important}}
</style></noscript>
</head>'''

def nav(active):
    links = ''.join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == active else ""}><span data-t="{n}">{n}</span></a>'
        for f, n in PAGES)
    mlinks = ''.join(
        f'<a href="{f}" style="--i:{i}"{" aria-current=\"page\"" if f == active else ""}><span>{n}</span></a>'
        for i, (f, n) in enumerate(PAGES))
    return f'''
<!-- PAGE TRANSITION -->
<div class="pt" id="pt" aria-hidden="true">
  <div class="pt-layer a"></div>
  <div class="pt-layer b"><span class="brand pt-logo"><img src="assets/logo.png" alt=""><span class="brand-fallback">MT <b>AUTO</b></span></span><span class="pt-label mono">MT Auto Care</span></div>
</div>

<!-- LOADER -->
<div class="loader" id="loader" aria-hidden="true">
  <div class="loader-top mono"><span>Car Care Studio</span><span>Chăm sóc · Phục hồi · Nâng cấp</span></div>
  <div class="loader-center"><span class="brand loader-logo"><img src="assets/logo.png" alt=""><span class="brand-fallback">MT <b>AUTO</b></span></span></div>
  <div class="loader-bottom">
    <div class="loader-num"><span><span id="loaderNum">0</span><sup>%</sup></span></div>
    <p class="mono loader-note">Đang chuẩn bị trải nghiệm của bạn</p>
  </div>
  <div class="loader-line" id="loaderLine"></div>
</div>

<div class="progress" id="progress" aria-hidden="true"></div>
<div class="cursor" id="cursor" aria-hidden="true"><div class="cursor-dot"><span>Xem</span></div></div>

<div class="fab" aria-label="Liên hệ nhanh">
  <a class="msg" href="{MSG}" target="_blank" rel="noopener" aria-label="Nhắn Messenger">{ICON_MSG}<span class="tip">Nhắn Messenger</span></a>
  <a class="zalo" href="{ZALO}" target="_blank" rel="noopener" aria-label="Chat Zalo">Zalo<span class="tip">Chat Zalo</span></a>
  <a class="call" href="tel:{PHONE}" aria-label="Gọi {PHONE_TXT}">{ICON_PHONE}<span class="tip">Gọi {PHONE_TXT}</span></a>
</div>
<button class="totop" id="totop" aria-label="Về đầu trang"><svg viewBox="0 0 58 58" aria-hidden="true"><circle id="totopRing" cx="29" cy="29" r="27"/></svg><span>↑</span></button>

<!-- HEADER -->
<header class="header" id="header">
  <div class="nav header-intro">
    <a href="index.html" class="brand" aria-label="MT Auto Care — Trang chủ"><img src="assets/logo.png" alt="MT Auto"><span class="brand-fallback">MT <b>AUTO</b></span></a>
    <nav class="nav-links" aria-label="Điều hướng chính">{links}</nav>
    <div class="nav-right">
      <span class="nav-clock" id="clock"></span>
      <a href="lien-he.html#booking" class="nav-book">Đặt lịch</a>
      <button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="menu">Menu</button>
    </div>
  </div>
</header>
<div class="menu" id="menu">
  <nav aria-label="Menu di động">{mlinks}</nav>
  <div class="menu-foot mono"><a href="tel:{PHONE}">{PHONE_TXT}</a><a href="{MAP_DIR}" target="_blank" rel="noopener">71A Tôn Thất Tùng, Pleiku</a></div>
</div>
'''

def nextp(href, label):
    return f'''
<a class="nextp" href="{href}" data-cursor="view" data-cursor-label="Đi">
  <span class="mono">Trang tiếp theo</span>
  <b>{label} <i>→</i></b>
</a>'''

FOOTER = f'''
<footer class="footer wrap">
  <div class="foot-row">
    <div><a href="index.html" class="brand" aria-label="MT Auto Care"><img src="assets/logo.png" alt="MT Auto"><span class="brand-fallback">MT <b>AUTO</b></span></a><p style="max-width:320px;color:rgba(247,246,243,.7)">Studio chăm sóc, phục hồi và nâng cấp ô tô.</p><p style="margin-top:14px"><a class="ulink" href="{MAP_DIR}" target="_blank" rel="noopener">{ADDRESS} ↗</a></p></div>
    <div><span class="mono">Trang</span><ul>{''.join(f'<li><a class="ulink" href="{f}">{n}</a></li>' for f, n in PAGES)}</ul></div>
    <div><span class="mono">Liên hệ</span><ul><li><a class="ulink" href="tel:{PHONE}">{PHONE_TXT}</a></li><li><a class="ulink" href="{ZALO}" target="_blank" rel="noopener">Zalo</a></li><li><a class="ulink" href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
    <div><span class="mono">Email</span><a class="ulink" href="mailto:{EMAIL}" style="word-break:break-all">{EMAIL}</a></div>
  </div>
  <div class="foot-mark" id="footMark" aria-label="MT Auto Care">MT AUTOCARE</div>
  <div class="foot-bottom mono"><span>© <span data-year>2026</span> MT Auto Care</span><span>Made with precision</span></div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

def page(fname, title, desc, main, nxt):
    html = head(title, desc, fname) + '\n<body class="is-loading">\n' + nav(fname) + '\n<main id="top">\n' + main + '\n</main>\n' + nxt + FOOTER
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(html)

def btn(label, href, extra=''):
    return f'<a href="{href}" class="btn"{extra}><span class="btn-roll"><span data-t="{label}">{label}</span></span><span class="btn-ico"><i>→</i><i>→</i></span></a>'

def visit(anchor):
    return f'''
<section class="sec wrap" id="{anchor}">
  <div class="visit">
    <div class="visit-info">
      <span class="label" data-fade>Địa chỉ</span>
      <h2 class="h-l" data-split>Ghé xưởng.</h2>
      <dl data-fade>
        <div><dt>Địa chỉ</dt><dd>{ADDRESS}<br><small class="muted" style="font-size:14px">({ADDRESS_OLD})</small></dd></div>
        <div><dt>Giờ làm việc</dt><dd>Vui lòng gọi trước để đặt lịch</dd></div>
        <div><dt>Hotline</dt><dd><a class="ulink" href="tel:{PHONE}">{PHONE_TXT}</a></dd></div>
      </dl>
      <div data-fade>{btn('Chỉ đường Google Maps', MAP_DIR, ' target="_blank" rel="noopener"')}</div>
    </div>
    <div class="visit-map" data-fade>
      <div class="grid-bg"></div>
      <div><div class="pin"></div><p>{ADDRESS}</p></div>
      <iframe src="{MAP_EMBED}" title="Bản đồ MT Auto — {ADDRESS}" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      <a class="map-dir mono" href="{MAP_DIR}" target="_blank" rel="noopener">Mở Google Maps ↗</a>
    </div>
  </div>
</section>'''

def phero(label, crumb, h1, lead, media=None):
    m = ''
    if media:
        m = f'<div class="phero-media" data-img style="--d:.35s"><img src="{u(media[0], 2000)}" alt="{media[1]}" data-speed="0.12" data-preload></div>'
    return f'''
<section class="phero">
  <div class="phero-top">
    <div class="crumbs mono hero-up" style="--d:.1s"><a href="index.html">Trang chủ</a><span>/</span><span>{crumb}</span></div>
    <p class="muted hero-up" style="--d:.5s">{lead}</p>
  </div>
  <span class="label hero-up" style="--d:.2s">{label}</span>
  <h1 data-split-now style="margin-top:22px">{h1}</h1>
  {m}
</section>'''

SERVICES = [
    ('cham-soc', '01', 'Detailing', 'Chăm sóc &amp; làm đẹp ô tô', 'Chăm sóc &amp; làm đẹp',
     'Làm sạch chuyên sâu, hiệu chỉnh và bảo vệ bề mặt — trả lại độ trong, độ bóng và cảm giác mới cho chiếc xe.',
     ['Vệ sinh chi tiết nội ngoại thất', 'Hiệu chỉnh &amp; đánh bóng sơn', 'Phủ bảo vệ bề mặt sơn', 'Vệ sinh khoang máy'], WASH),
    ('phuc-hoi', '02', 'Restoration', 'Phục hồi nội &amp; ngoại thất', 'Phục hồi nội ngoại thất',
     'Khôi phục những chi tiết đã xuống cấp theo thời gian, giữ trọn tinh thần nguyên bản của chiếc xe.',
     ['Phục hồi nội thất da', 'Phục hồi đèn pha, chi tiết nhựa', 'Xử lý vết xước, ố mốc', 'Làm mới khoang máy'], DETAIL),
    ('nang-cap', '03', 'Upgrades', 'Nâng cấp tiện nghi ô tô', 'Nâng cấp tiện nghi',
     'Những nâng cấp tinh tế, đúng nhu cầu sử dụng — tăng sự thoải mái mà vẫn hài hòa với thiết kế của xe.',
     ['Tiện nghi nội thất', 'Hệ thống âm thanh', 'Phụ kiện theo yêu cầu', 'Tư vấn cấu hình phù hợp'], INTERIOR),
]

# ----------------------------------------------------------------- HOME
cards = ''
for i, (sid, num, en, title, svc, desc, items, pid) in enumerate(SERVICES):
    t2 = ['Chăm sóc &amp;<br>làm đẹp ô tô', 'Phục hồi<br>nội &amp; ngoại thất', 'Nâng cấp<br>tiện nghi ô tô'][i]
    cards += f'''
    <article class="card" style="--i:{i}">
      <div class="card-in">
        <div class="card-body">
          <div class="card-top"><span class="card-num">{num}<sup>●</sup></span><span class="mono" style="opacity:.6">{en}</span></div>
          <div>
            <h3>{t2}</h3>
            <p>{desc}</p>
            <ul class="card-list">{''.join(f'<li><span>{it}</span><span>0{k+1}</span></li>' for k, it in enumerate(items[:3]))}</ul>
            {btn('Xem chi tiết', f'dich-vu.html#{sid}')}
          </div>
        </div>
        <div class="card-media" data-cursor="view">{img(pid, 1500, title.replace('&amp;', 'và'))}</div>
      </div>
      <div class="card-shade"></div>
    </article>'''

home = f'''
<section class="hero" id="hero">
  <div class="hero-frame" id="heroFrame">
    <div class="hero-img" id="heroImg"><img src="{u(HERO, 2200)}" alt="Xe thể thao trên đường" fetchpriority="high" data-preload></div>
  </div>
  <div class="hero-content" id="heroContent">
    <div class="hero-meta">
      <span class="label hero-up" style="--d:1.05s">MT Auto Care — Car Care Studio</span>
      <p class="hero-up" style="--d:1.2s">Chăm sóc, phục hồi và nâng cấp ô tô với sự chính xác của người làm nghề — để chiếc xe luôn ở phiên bản tốt nhất.</p>
    </div>
    <h1 class="hero-title" data-split-now>
      <span class="row"><span>Chăm chút</span><small>(01) Detailing<br>(02) Restoration<br>(03) Upgrades</small></span>
      <span class="row"><span>từng <span class="accent">chi tiết.</span></span></span>
    </h1>
    <div class="hero-bar mono hero-up" style="--d:1.4s">
      <span class="scroll"><i></i>Cuộn xuống</span>
      <span class="hide-s">Hotline {PHONE_TXT}</span>
      <a href="lien-he.html#booking" class="ulink">Đặt lịch hẹn ↗</a>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker-track" id="ticker">
    <div class="ticker-group"><span>Chăm sóc chuyên sâu</span><b>✦</b><span>Phục hồi nội ngoại thất</span><b>✦</b><span>Bảo vệ bề mặt sơn</span><b>✦</b><span>Nâng cấp tiện nghi</span><b>✦</b><span>Tư vấn tận tâm</span><b>✦</b></div>
  </div>
</div>

<section class="sec wrap" id="about">
  <div class="sec-head">
    <span class="label" data-fade>(01) Studio</span>
    <p class="intro-text" data-scrub>MT Auto Care là studio chăm sóc ô tô dành cho những người coi trọng chi tiết. Chúng tôi làm việc chậm rãi, chính xác và minh bạch — vì một chiếc xe đẹp không đến từ sự vội vàng.</p>
  </div>
  <div class="intro-grid">
    <div class="intro-a">
      <div class="intro-media" data-img>{img(RED, 1200, 'Xe thể thao màu đỏ', ' data-speed="0.1"')}</div>
      <div class="intro-cap mono muted" data-fade><span>Chi tiết / 01</span><span>Ngoại thất</span></div>
    </div>
    <div class="intro-b">
      <div class="intro-media" data-img style="--d:.15s">{img(DETAIL, 1400, 'Chi tiết ô tô', ' data-speed="-0.08"')}</div>
      <div class="intro-cap mono muted" data-fade><span>Chi tiết / 02</span><span>Hoàn thiện</span></div>
    </div>
  </div>
  <div class="feats">
    <div class="feat" data-fade><span class="mono">— A</span><h3>Chính xác</h3><p>Mỗi công đoạn có tiêu chuẩn rõ ràng, được kiểm tra trước khi bàn giao.</p></div>
    <div class="feat" data-fade style="--d:.1s"><span class="mono">— B</span><h3>Minh bạch</h3><p>Tư vấn dựa trên tình trạng thực tế, báo giá rõ ràng trước khi thực hiện.</p></div>
    <div class="feat" data-fade style="--d:.2s"><span class="mono">— C</span><h3>Tận tâm</h3><p>Lắng nghe nhu cầu riêng và đồng hành cùng bạn sau khi nhận xe.</p></div>
  </div>
</section>

<section class="sec wrap" id="services" style="padding-top:0">
  <div class="sec-head">
    <span class="label" data-fade>(02) Dịch vụ</span>
    <h2 class="h-xl" data-split>Ba chuyên môn. Một tiêu chuẩn.</h2>
  </div>
  <div class="stack">{cards}
  </div>
</section>

<section class="zoom" id="zoom" aria-label="Triết lý MT Auto Care">
  <div class="zoom-stick" id="zoomStick">
    <div class="zoom-img">{img(RED, 2200, 'Đường nét xe thể thao')}</div>
    <div class="zoom-hud mono"><span>(03) Triết lý</span><span id="zoomPct">000%</span></div>
    <div class="zoom-words" aria-hidden="true"><span class="l">Từng</span><span class="r">milimet.</span></div>
    <div class="zoom-cap">
      <h2 class="h-l">Không chỉ là chăm sóc xe. Đó là sự tôn trọng dành cho chiếc xe.</h2>
      <p>Mỗi chiếc xe đều xứng đáng được quan tâm đúng cách. MT Auto Care hướng tới trải nghiệm chỉn chu, rõ ràng và phù hợp với nhu cầu riêng của từng khách hàng.</p>
    </div>
  </div>
</section>

<section class="sec wrap" id="process">
  <div class="process-grid">
    <aside class="process-aside">
      <span class="label" data-fade>(04) Quy trình</span>
      <h2 class="h-l" data-split>Từ lúc bạn đến, đến lúc bạn lăn bánh.</h2>
      <div class="process-count" aria-hidden="true">
        <span class="big"><span id="pcount"><b>01</b><b>02</b><b>03</b><b>04</b></span></span>
        <span class="mono muted" style="padding-bottom:6px">/ 04</span>
      </div>
    </aside>
    <div class="process-steps">
      <div class="pstep"><span class="mono">Bước 01</span><h3>Tiếp nhận &amp; lắng nghe</h3><p>Trao đổi về tình trạng xe, thói quen sử dụng và điều bạn mong muốn. Mọi giải pháp đều bắt đầu từ việc hiểu đúng nhu cầu.</p><div class="tags"><span>Trao đổi</span><span>Ghi nhận</span></div></div>
      <div class="pstep"><span class="mono">Bước 02</span><h3>Kiểm tra &amp; đề xuất</h3><p>Đánh giá thực tế từng hạng mục, đề xuất phương án phù hợp kèm chi phí và thời gian rõ ràng trước khi bắt đầu.</p><div class="tags"><span>Đánh giá</span><span>Báo giá</span></div></div>
      <div class="pstep"><span class="mono">Bước 03</span><h3>Thực hiện tỉ mỉ</h3><p>Từng công đoạn được thực hiện cẩn thận theo quy chuẩn kỹ thuật, với sản phẩm và dụng cụ phù hợp cho từng bề mặt.</p><div class="tags"><span>Kỹ thuật</span><span>Kiểm soát</span></div></div>
      <div class="pstep"><span class="mono">Bước 04</span><h3>Bàn giao &amp; đồng hành</h3><p>Kiểm tra cùng bạn khi nhận xe, hướng dẫn bảo quản và sẵn sàng hỗ trợ trong suốt quá trình sử dụng.</p><div class="tags"><span>Bàn giao</span><span>Hỗ trợ</span></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="gallery" aria-label="Hình ảnh">
  <div class="gallery-head wrap">
    <h2 class="h-l" data-split>Chi tiết tạo nên khác biệt.</h2>
    <div data-fade>{btn('Xem công trình', 'cong-trinh.html')}</div>
  </div>
  <div class="grow">
    <figure class="w">{img(HERO, 1000, 'Xe thể thao')}<figcaption>MT / 01</figcaption></figure>
    <figure class="t">{img(PORSCHE, 700, 'Xe thể thao', fallback=WASH)}<figcaption>MT / 02</figcaption></figure>
    <figure class="w">{img(INTERIOR, 1000, 'Nội thất ô tô')}<figcaption>MT / 03</figcaption></figure>
    <figure class="t">{img(DETAIL, 700, 'Chi tiết ô tô')}<figcaption>MT / 04</figcaption></figure>
    <figure class="w">{img(RED, 1000, 'Xe thể thao màu đỏ')}<figcaption>MT / 05</figcaption></figure>
  </div>
  <div class="grow">
    <figure class="t">{img(WASH, 700, 'Ô tô sau chăm sóc')}<figcaption>MT / 06</figcaption></figure>
    <figure class="w">{img(MUSTANG, 1000, 'Xe cổ điển', fallback=HERO)}<figcaption>MT / 07</figcaption></figure>
    <figure class="t">{img(RED, 700, 'Đường nét xe')}<figcaption>MT / 08</figcaption></figure>
    <figure class="w">{img(ORANGE, 1000, 'Siêu xe', fallback=INTERIOR)}<figcaption>MT / 09</figcaption></figure>
    <figure class="t">{img(HERO, 700, 'Xe thể thao')}<figcaption>MT / 10</figcaption></figure>
  </div>
</section>

'''+ visit('ghe-xuong') + '''
<section class="contact wrap">
  <span class="label" data-fade>(05) Đặt lịch</span>
  <a href="lien-he.html#booking" class="cta-big" data-cursor="view" data-cursor-label="Đặt lịch"><span data-split>Hãy bắt đầu</span><br><span data-split style="--d:.1s">cùng MT</span> <span class="arrow">↗</span></a>
  <div class="contact-grid">
    <div class="contact-info" data-fade>
      <div><span class="mono">Hotline</span><a class="big ulink" href="tel:{PHONE}">{PHONE_TXT}</a></div>
    </div>
    <div class="contact-info" data-fade style="--d:.1s;grid-column:7/13">
      <div><span class="mono">Xưởng</span><a class="big ulink" href="{MAP_DIR}" target="_blank" rel="noopener">71A Tôn Thất Tùng, Pleiku ↗</a></div>
      <div><span class="mono">Facebook</span><a class="big ulink" href="{FB}" target="_blank" rel="noopener">/mt.autochamsocxe</a></div>
    </div>
  </div>
</section>'''
page('index.html', 'MT Auto Care — Studio chăm sóc ô tô',
     'MT Auto Care — studio chăm sóc, phục hồi và nâng cấp ô tô. Hotline 0823 418 418.',
     home, nextp('dich-vu.html', 'Dịch vụ'))

# ----------------------------------------------------------------- SERVICES
hrows = ''.join(f'''
    <a class="hrow" href="#{sid}"><span class="mono">({num})</span><h3>{title}</h3><p>{desc}</p><span class="go">→</span></a>'''
    for sid, num, en, title, svc, desc, items, pid in SERVICES)
hfloat = ''.join(f'<img src="{u(pid, 600)}" alt="">' for *_, pid in SERVICES)
snav = ''.join(f'<a href="#{sid}"><i></i>{svc.replace("&amp;", "&")}</a>' for sid, num, en, title, svc, desc, items, pid in SERVICES)
sblocks = ''.join(f'''
      <article class="sblock" id="{sid}">
        <div class="sblock-media" data-img>{img(pid, 1100, title.replace('&amp;', 'và'), ' data-speed="0.1"')}</div>
        <div>
          <span class="mono" data-fade>({num}) {en}</span>
          <h2 data-split>{title}</h2>
          <p data-fade>{desc}</p>
          <ul data-fade>{''.join(f'<li>{it}</li>' for it in items)}</ul>
          <div data-fade>{btn('Đặt lịch dịch vụ', 'lien-he.html#booking', f' data-service="{svc.replace("&amp;", "&")}"')}</div>
        </div>
      </article>''' for sid, num, en, title, svc, desc, items, pid in SERVICES)

services = phero('Dịch vụ — Services', 'Dịch vụ', 'Dịch vụ <span class="accent">chuyên sâu.</span>',
                 'Ba nhóm dịch vụ cốt lõi, cùng một tiêu chuẩn: tỉ mỉ, minh bạch và đúng nhu cầu của chiếc xe.') + f'''

<section class="sec wrap">
  <div class="hindex">{hrows}
  </div>
  <div class="hfloat" aria-hidden="true">{hfloat}</div>
</section>

<section class="sec wrap" style="padding-top:0">
  <div class="sdetail">
    <nav class="snav mono" aria-label="Các dịch vụ">{snav}</nav>
    <div class="sblocks">{sblocks}
    </div>
  </div>
</section>

<section class="sec wrap" id="faq" style="padding-top:0">
  <div class="faq-grid">
    <div>
      <span class="label" data-fade>Hỏi đáp</span>
      <h2 class="h-l" style="margin-top:24px" data-split>Những điều bạn có thể muốn biết.</h2>
    </div>
    <div class="faq-list" data-fade>
      <div class="faq-item open"><button class="faq-q" aria-expanded="true">Tôi có cần đặt lịch trước không?<i></i></button><div class="faq-a"><div><p>Nên đặt lịch trước để MT Auto Care chủ động sắp xếp thời gian và chuẩn bị tốt nhất cho chiếc xe của bạn. Bạn có thể gọi hotline, nhắn Zalo hoặc Messenger.</p></div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Chi phí dịch vụ được tính như thế nào?<i></i></button><div class="faq-a"><div><p>Chi phí phụ thuộc vào dòng xe, tình trạng thực tế và hạng mục bạn chọn. Chúng tôi kiểm tra và báo giá rõ ràng trước khi bắt đầu thực hiện.</p></div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Thời gian thực hiện mất bao lâu?<i></i></button><div class="faq-a"><div><p>Mỗi dịch vụ có thời gian khác nhau. Thời gian dự kiến sẽ được thông báo cụ thể khi tư vấn để bạn chủ động sắp xếp.</p></div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Tôi chưa biết xe mình cần gì, phải làm sao?<i></i></button><div class="faq-a"><div><p>Bạn chỉ cần mô tả tình trạng xe và mong muốn của mình. Đội ngũ MT Auto Care sẽ kiểm tra và tư vấn phương án phù hợp nhất với nhu cầu và ngân sách.</p></div></div></div>
    </div>
  </div>
</section>'''
page('dich-vu.html', 'Dịch vụ — MT Auto Care',
     'Chăm sóc & làm đẹp, phục hồi nội ngoại thất và nâng cấp tiện nghi ô tô tại MT Auto Care.',
     services, nextp('cong-trinh.html', 'Công trình'))

# ----------------------------------------------------------------- WORKS
WORKS = [
    ('cham-soc', 'Chăm sóc', 'Đánh bóng &amp; phủ bảo vệ', HERO, 'wide'),
    ('phuc-hoi', 'Phục hồi', 'Phục hồi chi tiết ngoại thất', DETAIL, ''),
    ('nang-cap', 'Nâng cấp', 'Nâng cấp nội thất', INTERIOR, ''),
    ('cham-soc', 'Chăm sóc', 'Vệ sinh chi tiết toàn xe', WASH, ''),
    ('cham-soc', 'Chăm sóc', 'Làm đẹp ngoại thất', RED, 'wide'),
    ('phuc-hoi', 'Phục hồi', 'Phục hồi xe cổ điển', MUSTANG, 'wide'),
    ('nang-cap', 'Nâng cấp', 'Phụ kiện theo yêu cầu', PORSCHE, ''),
    ('phuc-hoi', 'Phục hồi', 'Làm mới bề mặt', ORANGE, ''),
]
FB_FOR = {MUSTANG: HERO, PORSCHE: WASH, ORANGE: INTERIOR}
works = ''.join(f'''
    <figure class="work {wide}" data-cat="{cat}" data-title="{t.replace('&amp;', '&')}" tabindex="0" data-cursor="view" data-fade style="--d:{(i % 3) * .08:.2f}s">{img(pid, 1400 if wide else 800, t.replace('&amp;', 'và'), fallback=FB_FOR.get(pid))}<figcaption><b>{t}</b><span class="mono">{lbl}</span></figcaption></figure>'''
    for i, (cat, lbl, t, pid, wide) in enumerate(WORKS))

works_page = phero('Công trình — Works', 'Công trình', 'Công trình <span class="accent">đã thực hiện.</span>',
                   'Một vài khoảnh khắc từ xưởng. Hình ảnh hiện là ảnh minh họa và sẽ được thay bằng ảnh thực tế của MT Auto Care.') + f'''

<section class="sec wrap" style="padding-top:clamp(60px,10vh,110px)">
  <div class="filters" role="group" aria-label="Lọc theo dịch vụ">
    <button class="on" data-filter="all">Tất cả</button>
    <button data-filter="cham-soc">Chăm sóc</button>
    <button data-filter="phuc-hoi">Phục hồi</button>
    <button data-filter="nang-cap">Nâng cấp</button>
  </div>
  <div class="works">{works}
  </div>
</section>

<section class="sec wrap" style="padding-top:0">
  <div class="sec-head">
    <span class="label" data-fade>Trước / Sau</span>
    <h2 class="h-l" data-split>Kéo để thấy sự khác biệt.</h2>
  </div>
  <div class="ba" data-fade data-cursor="view" data-cursor-label="Kéo" aria-label="So sánh trước và sau, dùng phím mũi tên để kéo">
    <img src="{u(RED, 1800)}" alt="Sau khi chăm sóc">
    <img class="before" src="{u(RED, 1800)}" alt="Trước khi chăm sóc">
    <span class="tag l">Trước</span><span class="tag r">Sau</span>
    <span class="handle"></span>
  </div>
  <p class="ba-note mono">Ảnh minh họa — sẽ thay bằng cặp ảnh trước/sau thực tế.</p>
</section>

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Xem ảnh">
  <figure><img alt=""><figcaption><span class="cap"></span><span class="num mono"></span></figcaption></figure>
  <button class="x" aria-label="Đóng">✕</button>
  <button class="prev" aria-label="Ảnh trước">←</button>
  <button class="next" aria-label="Ảnh sau">→</button>
</div>'''
page('cong-trinh.html', 'Công trình — MT Auto Care',
     'Hình ảnh các công trình chăm sóc, phục hồi và nâng cấp ô tô tại MT Auto Care.',
     works_page, nextp('lien-he.html', 'Liên hệ'))

# ----------------------------------------------------------------- CONTACT
contact = phero('Liên hệ — Contact', 'Liên hệ', 'Ghé thăm <span class="accent">MT Auto.</span>',
                'Gọi điện, nhắn tin hoặc để lại thông tin — chúng tôi sẽ liên hệ lại để tư vấn cho chiếc xe của bạn.') + f'''

<section class="sec wrap" style="padding-top:clamp(60px,10vh,110px)">
  <div class="cards">
    <a class="ccard" href="tel:{PHONE}" data-fade><span class="mono">Hotline</span><b>{PHONE_TXT}</b><span class="go">→</span></a>
    <a class="ccard" href="{ZALO}" target="_blank" rel="noopener" data-fade style="--d:.08s"><span class="mono">Zalo</span><b>Chat Zalo<br>{PHONE_TXT}</b><span class="go">→</span></a>
    <a class="ccard" href="{FB}" target="_blank" rel="noopener" data-fade style="--d:.16s"><span class="mono">Facebook</span><b>/mt.autochamsocxe</b><span class="go">→</span></a>
    <a class="ccard wide" href="{MAP_DIR}" target="_blank" rel="noopener" data-fade><span class="mono">Địa chỉ xưởng</span><b>71A Tôn Thất Tùng,<br>Phường Pleiku, Gia Lai</b><span class="go">→</span></a>
  </div>
</section>

<section class="contact wrap" id="booking">
  <span class="label" data-fade>Đặt lịch hẹn</span>
  <h2 class="cta-big" style="font-size:clamp(52px,9vw,170px)"><span data-split>Để lại thông tin,</span><br><span data-split style="--d:.1s">MT gọi lại ngay.</span></h2>
  <div class="contact-grid">
    <div class="contact-info" data-fade>
      <div><span class="mono">Hotline</span><a class="big ulink" href="tel:{PHONE}">{PHONE_TXT}</a></div>
      <div><span class="mono">Email</span><a class="big ulink" href="mailto:{EMAIL}" style="word-break:break-all">{EMAIL}</a></div>
      <div><span class="mono">Phản hồi</span><p style="color:rgba(247,246,243,.7);max-width:340px">Chúng tôi sẽ liên hệ lại để tư vấn chi tiết cho chiếc xe của bạn.</p></div>
    </div>
    <form class="form" id="booking-form" data-fade style="--d:.1s" novalidate>
      <div class="field full"><label>Dịch vụ quan tâm</label>
        <div class="chips" role="radiogroup" aria-label="Dịch vụ quan tâm">
          <label class="chip"><input type="radio" name="service" value="Chăm sóc & làm đẹp" checked><span>Chăm sóc &amp; làm đẹp</span></label>
          <label class="chip"><input type="radio" name="service" value="Phục hồi nội ngoại thất"><span>Phục hồi</span></label>
          <label class="chip"><input type="radio" name="service" value="Nâng cấp tiện nghi"><span>Nâng cấp</span></label>
          <label class="chip"><input type="radio" name="service" value="Khác"><span>Khác</span></label>
        </div>
      </div>
      <div class="field"><label for="f-name">Họ và tên</label><input id="f-name" name="name" placeholder="Nguyễn Văn A" autocomplete="name"></div>
      <div class="field"><label for="f-phone">Số điện thoại</label><input id="f-phone" name="phone" type="tel" placeholder="09xx xxx xxx" autocomplete="tel"></div>
      <div class="field full"><label for="f-car">Dòng xe</label><input id="f-car" name="car" placeholder="Ví dụ: Mercedes C300 2022"></div>
      <div class="field full"><label for="f-msg">Lời nhắn</label><textarea id="f-msg" name="message" rows="2" placeholder="Mô tả ngắn nhu cầu của bạn"></textarea></div>
      <div class="form-foot">
        <small id="formNote">Nút gửi sẽ mở ứng dụng email của bạn với nội dung đã điền sẵn.</small>
        <button class="btn light" type="submit"><span class="btn-roll"><span data-t="Gửi yêu cầu">Gửi yêu cầu</span></span><span class="btn-ico"><i>→</i><i>→</i></span></button>
      </div>
    </form>
  </div>
</section>

'''+ visit('map') + ''''''
page('lien-he.html', 'Liên hệ — MT Auto Care',
     'Liên hệ MT Auto Care: hotline 0823 418 418, Zalo, Facebook và đặt lịch chăm sóc xe.',
     contact, nextp('index.html', 'Trang chủ'))
print('ok')
