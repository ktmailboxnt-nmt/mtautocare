"""Generate the four MT Auto Care pages with shared head, header and footer."""
import sys, os, hashlib

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

def im(name, alt, extra='', lazy=True):
    """A real photo from assets/img (exported from the shop's Facebook photos)."""
    ld = ' loading="lazy"' if lazy else ''
    return f'<img{ld} src="assets/img/{name}.jpg" alt="{alt}"{extra}>'

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

ICON_FB = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.87.25-1.46 1.5-1.46h1.6V4.46A21 21 0 0 0 14.3 4.3c-2.3 0-3.8 1.4-3.8 3.95v2.25H8v3h2.5V21z"/></svg>'

PAGES = [
    ('index.html', 'Trang chủ'),
    ('dich-vu.html', 'Dịch vụ'),
    ('cong-trinh.html', 'Công trình'),
    ('lien-he.html', 'Liên hệ'),
]

def ver(rel):
    """Content hash, so browsers fetch css/js again after every change."""
    return hashlib.md5(open(os.path.join(OUT, rel), 'rb').read()).hexdigest()[:8]

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
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap&subset=vietnamese" rel="stylesheet">
<script>document.documentElement.classList.add('js');try{{if(sessionStorage.getItem('mt-pt')==='1')document.documentElement.classList.add('pt-arrive')}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/css/style.css?v={ver('assets/css/style.css')}">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"AutoRepair","name":"MT Auto Care","image":"{SITE_URL}assets/og.jpg","url":"{SITE_URL}","telephone":"+84823418418","email":"{EMAIL}","address":{{"@type":"PostalAddress","streetAddress":"71A Tôn Thất Tùng","addressLocality":"Phường Pleiku","addressRegion":"Gia Lai","addressCountry":"VN"}},"geo":{{"@type":"GeoCoordinates","latitude":{LAT},"longitude":{LNG}}},"hasMap":"{MAP_DIR}","priceRange":"$$","openingHoursSpecification":[{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"07:15","closes":"18:00"}}],"areaServed":"Gia Lai","sameAs":["{FB}","{MAP_DIR}"]}}</script>
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
  <div class="loader-top mono"><span>Trung tâm chăm sóc xe ô tô</span><span>Độ đèn · Màn hình · Phanh – mâm – body · Chăm sóc</span></div>
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
  <a class="fb" href="{FB}" target="_blank" rel="noopener" aria-label="Trang Facebook MT Auto">{ICON_FB}<span class="tip">Facebook MT Auto</span></a>
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
    <div><a href="index.html" class="brand" aria-label="MT Auto Care"><img src="assets/logo.png" alt="MT Auto"><span class="brand-fallback">MT <b>AUTO</b></span></a><p style="max-width:320px;color:rgba(247,246,243,.7)">Trung tâm chăm sóc &amp; nâng cấp ô tô tại Pleiku — Nâng niu xế yêu.</p><p style="margin-top:14px"><a class="ulink" href="{MAP_DIR}" target="_blank" rel="noopener">{ADDRESS} ↗</a></p></div>
    <div><span class="mono">Trang</span><ul>{''.join(f'<li><a class="ulink" href="{f}">{n}</a></li>' for f, n in PAGES)}</ul></div>
    <div><span class="mono">Liên hệ</span><ul><li><a class="ulink" href="tel:{PHONE}">{PHONE_TXT}</a></li><li><a class="ulink" href="{ZALO}" target="_blank" rel="noopener">Zalo</a></li><li><a class="ulink" href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
    <div><span class="mono">Email</span><a class="ulink" href="mailto:{EMAIL}" style="word-break:break-all">{EMAIL}</a></div>
  </div>
  <div class="foot-mark" id="footMark" aria-label="MT Auto Care">MT AUTOCARE</div>
  <div class="foot-bottom mono"><span>© <span data-year>2026</span> MT Auto Care</span><span>Made with precision</span></div>
</footer>
<script src="assets/js/main.js?v={ver('assets/js/main.js')}"></script>
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
        <div><dt>Giờ làm việc</dt><dd>7:15 – 18:00<br><small class="muted" style="font-size:14px">Nên gọi trước để được sắp lịch</small></dd></div>
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
        m = f'<div class="phero-media" data-img style="--d:.35s"><img src="assets/img/{media[0]}.jpg" alt="{media[1]}" style="object-position:{media[2] if len(media) > 2 else 'center'}" data-speed="0.12" data-preload></div>'
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

# Real service groups, taken from the work the shop posts on Facebook.
# (id, number, english tag, title, short name, description, items, card photo, detail photo)
SERVICES = [
    ('do-den', '01', 'Lighting', 'Độ đèn &amp; ánh sáng', 'Độ đèn',
     'Nâng cấp bi LED, đèn gầm và bóng LED chính hãng — tăng sáng rõ rệt, chuẩn đường cắt, an toàn hơn khi đi đêm và đường đèo.',
     ['Bi LED X-Light V12, V20, F10', 'Bi LED Steelmate C3-Pro', 'Đèn gầm, đèn sương mù', 'Tháo lắp, căn chỉnh chuẩn kỹ thuật'], 'den-c3pro', 'den-gam'),
    ('man-hinh', '02', 'Multimedia', 'Màn hình, Android box &amp; âm thanh', 'Màn hình &amp; âm thanh',
     'Biến khoang lái thành trung tâm giải trí thông minh: Android box, màn hình lớn, camera hành trình và âm thanh — lắp gọn gàng, đúng xe.',
     ['Android box HTD D14 Ultra', 'Màn hình Gotech, iCar Elliview, Zestech', 'Loa sub Steelmate', 'Camera hành trình 70mai'], 'man-d14', 'man-zestech'),
    ('phanh-mam', '03', 'Performance', 'Phanh, mâm, gầm &amp; body', 'Phanh, mâm, gầm &amp; body',
     'Heo phanh hiệu năng cao, mâm thể thao, ốp bảo vệ gầm và body kit — xe đẹp hơn, thể thao hơn, an toàn và bền bỉ hơn trên mọi cung đường.',
     ['Heo phanh Brembo, AMG', 'Mâm thể thao, ốc mâm Rays', 'Body kit, nâng cấp ngoại thất', 'Ốp bảo vệ gầm B-F'], 'phanh-brembo', 'mam-do'),
    ('cham-soc', '04', 'Care', 'Chăm sóc &amp; nội thất', 'Chăm sóc &amp; nội thất',
     'Chăm sóc định kỳ và làm mới khoang lái: phủ kính, thay dầu, gạt mưa, vô lăng carbon, bọc da — để xe luôn sạch đẹp và dễ chịu.',
     ['Phủ kính Meguiar’s, gạt mưa Bosch', 'Thay dầu nhớt, vệ sinh khoang máy', 'Vô lăng carbon', 'Bọc da, bọc nỉ nội thất'], 'vo-lang-carbon', 'cs-phu-kinh'),
]
CARD_TITLES = ['Độ đèn &amp;<br>ánh sáng', 'Màn hình &amp;<br>âm thanh', 'Phanh, mâm,<br>gầm &amp; body', 'Chăm sóc<br>&amp; nội thất']
plain = lambda t: t.replace('&amp;', '&')

REELS = [
    ('reel1', 'Nâng cấp màn hình Android', 'Mazda'),
    ('reel2', 'Lắp màn hình &amp; âm thanh', 'Hyundai'),
    ('reel3', 'Một ngày ở xưởng MT Auto', 'Pleiku'),
]

def reels(label):
    items = ''.join(f'''
    <figure class="reel" data-fade style="--d:{i * .08:.2f}s">
      <button class="reel-phone" data-full="assets/video/{rid}.mp4" data-cursor="view" data-cursor-label="Xem" aria-label="Xem video: {plain(t)}">
        <video muted loop playsinline preload="none" poster="assets/video/{rid}.jpg" data-src="assets/video/{rid}-loop.mp4"></video>
        <span class="reel-play" aria-hidden="true">▶</span>
      </button>
      <figcaption><b>{t}</b><span class="mono">{car}</span></figcaption>
    </figure>''' for i, (rid, t, car) in enumerate(REELS))
    return f'''
<section class="sec wrap reels-sec" id="video">
  <div class="sec-head">
    <span class="label" data-fade>{label}</span>
    <div>
      <h2 class="h-l" data-split>Thực tế tại xưởng.</h2>
      <p class="muted" data-fade style="margin-top:18px;max-width:440px">Bấm vào video để xem đầy đủ, có âm thanh.</p>
    </div>
  </div>
  <div class="reels">{items}
  </div>
</section>'''

VPLAYER = '''
<div class="vp" id="vp" role="dialog" aria-modal="true" aria-label="Xem video">
  <video controls playsinline preload="none"></video>
  <button class="x" aria-label="Đóng">✕</button>
</div>'''

# ----------------------------------------------------------------- HOME
cards = ''
for i, (sid, num, en, title, svc, desc, items, pic, _) in enumerate(SERVICES):
    cards += f'''
    <article class="card" style="--i:{i}">
      <div class="card-in">
        <div class="card-body">
          <div class="card-top"><span class="card-num">{num}<sup>●</sup></span><span class="mono" style="opacity:.6">{en}</span></div>
          <div>
            <h3>{CARD_TITLES[i]}</h3>
            <p>{desc}</p>
            <ul class="card-list">{''.join(f'<li><span>{it}</span><span>0{k+1}</span></li>' for k, it in enumerate(items[:3]))}</ul>
            {btn('Xem chi tiết', f'dich-vu.html#{sid}')}
          </div>
        </div>
        <div class="card-media" data-cursor="view">{im(pic, plain(title))}</div>
      </div>
      <div class="card-shade"></div>
    </article>'''

GALLERY = [
    [('den-steelmate', 't', 'Bi LED Steelmate'), ('phanh-amg', 'w', 'Heo phanh AMG'), ('man-d14-mazda', 't', 'D14 Ultra — Mazda'),
     ('gam-vinfast', 'w', 'Ốp gầm B-F — VinFast'), ('vo-lang-kia', 't', 'Khoang lái sau nâng cấp')],
    [('mam-do', 't', 'Mâm &amp; heo Brembo'), ('cs-meguiars', 'w', 'Phủ kính Meguiar’s'), ('loa-steelmate', 't', 'Loa sub Steelmate'),
     ('xlight-cover', 'w', 'Độ bi X-Light V20'), ('noi-that-da', 't', 'Bọc da bệ tì tay')],
]
rows = ''.join('\n  <div class="grow">' + ''.join(
    f'\n    <figure class="{c}">{im(n, plain(t))}<figcaption>{t}</figcaption></figure>' for n, c, t in row) + '\n  </div>' for row in GALLERY)

home = f'''
<section class="hero" id="hero">
  <div class="hero-frame" id="heroFrame">
    <div class="hero-img" id="heroImg">
      {im('hero', 'Ford Everest tại xưởng MT Auto', ' fetchpriority="high" data-preload', lazy=False)}
      <video class="hero-video" muted loop playsinline preload="none" poster="assets/video/hero-m.jpg" data-src="assets/video/hero-m.mp4" aria-hidden="true"></video>
    </div>
    <div class="hero-dv" aria-hidden="true">
      <video class="hdv-bg" muted loop playsinline preload="none" poster="assets/video/hero-d.jpg" data-src="assets/video/hero-d.mp4"></video>
      <video class="hdv-fg" muted loop playsinline preload="none" poster="assets/video/hero-d.jpg" data-src="assets/video/hero-d.mp4"></video>
    </div>
  </div>
  <div class="hero-content" id="heroContent">
    <div class="hero-meta">
      <span class="label hero-up" style="--d:1.05s">MT Auto — Nâng niu xế yêu</span>
      <p class="hero-up" style="--d:1.2s">Trung tâm chăm sóc và nâng cấp ô tô tại Pleiku: độ đèn, màn hình, phanh, mâm, body kit và chăm sóc xe — làm tỉ mỉ, tư vấn đúng nhu cầu.</p>
    </div>
    <h1 class="hero-title" data-split-now>
      <span class="row"><span>Chăm chút</span><small>(01) Độ đèn<br>(02) Màn hình<br>(03) Phanh – mâm – body<br>(04) Chăm sóc</small></span>
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
    <div class="ticker-group"><span>Độ đèn bi LED</span><b>✦</b><span>Màn hình Android</span><b>✦</b><span>Phanh Brembo</span><b>✦</b><span>Mâm thể thao</span><b>✦</b><span>Ốp gầm</span><b>✦</b><span>Body kit</span><b>✦</b><span>Phủ kính</span><b>✦</b><span>Vô lăng carbon</span><b>✦</b><span>Âm thanh</span><b>✦</b></div>
  </div>
</div>

<section class="sec wrap" id="about">
  <div class="sec-head">
    <span class="label" data-fade>(01) Về MT Auto</span>
    <p class="intro-text" data-scrub>MT Auto là nơi chăm sóc ô tô dành cho những người *coi trọng chi tiết.* Chúng tôi làm việc *chậm rãi, chính xác và minh bạch* — vì một chiếc xe đẹp không đến từ sự vội vàng.</p>
  </div>
  <div class="intro-grid">
    <div class="intro-a">
      <div class="intro-media" data-img>{im('storefront', 'Mặt tiền xưởng MT Auto', ' data-speed="0.1"')}</div>
      <div class="intro-cap mono muted" data-fade><span>Xưởng / 71A Tôn Thất Tùng</span><span>Pleiku</span></div>
    </div>
    <div class="intro-b">
      <div class="intro-media" data-img style="--d:.15s">{im('shop-xpander', 'Mitsubishi Xpander độ bi LED tại MT Auto', ' data-speed="-0.08"')}</div>
      <div class="intro-cap mono muted" data-fade><span>Bàn giao / Mitsubishi Xpander</span><span>Độ bi LED</span></div>
    </div>
  </div>
  <div class="feats">
    <div class="feat" data-fade><span class="mono">— A</span><h3>Hàng chính hãng</h3><p>Sản phẩm từ các thương hiệu uy tín như X-Light, Steelmate, Brembo, Bosch, Meguiar’s.</p></div>
    <div class="feat" data-fade style="--d:.1s"><span class="mono">— B</span><h3>Tư vấn đúng xe</h3><p>Đề xuất món đồ phù hợp với dòng xe, nhu cầu và ngân sách — báo giá rõ trước khi làm.</p></div>
    <div class="feat" data-fade style="--d:.2s"><span class="mono">— C</span><h3>Lắp đặt chỉn chu</h3><p>Đội thợ làm cẩn thận, gọn gàng, kiểm tra kỹ cùng bạn trước khi bàn giao.</p></div>
  </div>
</section>

<section class="sec wrap" id="services" style="padding-top:0">
  <div class="sec-head">
    <span class="label" data-fade>(02) Dịch vụ</span>
    <h2 class="h-xl" data-split>Bốn nhóm dịch vụ. Một tiêu chuẩn.</h2>
  </div>
  <div class="stack">{cards}
  </div>
</section>

<section class="zoom" id="zoom" aria-label="Xưởng MT Auto">
  <div class="zoom-stick" id="zoomStick">
    <div class="zoom-img">{im('shop-overhead', 'Toàn cảnh xưởng MT Auto')}</div>
    <div class="zoom-hud mono"><span>(03) Xưởng MT Auto</span><span id="zoomPct">000%</span></div>
    <div class="zoom-words" aria-hidden="true"><span class="l">Nâng niu</span><span class="r">xế yêu.</span></div>
    <div class="zoom-cap">
      <h2 class="h-l">Chiếc xe của bạn, được chăm như xe của chúng tôi.</h2>
      <p>Không gian xưởng rộng rãi, sạch sẽ cùng đội thợ tận tâm — mỗi chiếc xe ra về đều đẹp hơn, tiện nghi hơn và an toàn hơn.</p>
    </div>
  </div>
</section>
''' + reels('(04) Video') + f'''
<section class="sec wrap" id="process">
  <div class="process-grid">
    <aside class="process-aside">
      <span class="label" data-fade>(05) Quy trình</span>
      <h2 class="h-l" data-split>Từ lúc bạn đến, đến lúc bạn lăn bánh.</h2>
      <div class="process-count" aria-hidden="true">
        <span class="big"><span id="pcount"><b>01</b><b>02</b><b>03</b><b>04</b></span></span>
        <span class="mono muted" style="padding-bottom:6px">/ 04</span>
      </div>
    </aside>
    <div class="process-steps">
      <div class="pstep"><span class="mono">Bước 01</span><h3>Tiếp nhận &amp; tư vấn</h3><p>Trao đổi về dòng xe, thói quen sử dụng và điều bạn mong muốn để chọn đúng món đồ phù hợp.</p><div class="tags"><span>Trao đổi</span><span>Tư vấn</span></div></div>
      <div class="pstep"><span class="mono">Bước 02</span><h3>Báo giá rõ ràng</h3><p>Đưa ra phương án, sản phẩm và chi phí cụ thể trước khi bắt đầu — không phát sinh bất ngờ.</p><div class="tags"><span>Phương án</span><span>Báo giá</span></div></div>
      <div class="pstep"><span class="mono">Bước 03</span><h3>Lắp đặt tỉ mỉ</h3><p>Đội thợ tháo lắp cẩn thận, đi dây gọn gàng, giữ nguyên zin những gì cần giữ.</p><div class="tags"><span>Kỹ thuật</span><span>Gọn gàng</span></div></div>
      <div class="pstep"><span class="mono">Bước 04</span><h3>Bàn giao &amp; hỗ trợ</h3><p>Kiểm tra cùng bạn khi nhận xe, hướng dẫn sử dụng và sẵn sàng hỗ trợ về sau.</p><div class="tags"><span>Bàn giao</span><span>Hỗ trợ</span></div></div>
    </div>
  </div>
</section>

<section class="gallery" id="gallery" aria-label="Hình ảnh">
  <div class="gallery-head wrap">
    <h2 class="h-l" data-split>Chi tiết tạo nên khác biệt.</h2>
    <div data-fade>{btn('Xem công trình', 'cong-trinh.html')}</div>
  </div>{rows}
</section>
''' + visit('ghe-xuong') + f'''
<section class="contact wrap">
  <span class="label" data-fade>(06) Đặt lịch</span>
  <a href="lien-he.html#booking" class="cta-big" data-cursor="view" data-cursor-label="Đặt lịch"><span data-split>Hãy bắt đầu</span><br><span data-split style="--d:.1s">cùng MT</span> <span class="arrow">↗</span></a>
  <div class="contact-grid">
    <div class="contact-info" data-fade>
      <div><span class="mono">Hotline</span><a class="big ulink" href="tel:{PHONE}">{PHONE_TXT}</a></div>
    </div>
    <div class="contact-info right" data-fade style="--d:.1s">
      <div><span class="mono">Xưởng</span><a class="big ulink" href="{MAP_DIR}" target="_blank" rel="noopener">71A Tôn Thất Tùng, Pleiku ↗</a></div>
      <div><span class="mono">Facebook</span><a class="big ulink" href="{FB}" target="_blank" rel="noopener">/mt.autochamsocxe</a></div>
    </div>
  </div>
</section>''' + VPLAYER
page('index.html', 'MT Auto — Trung tâm chăm sóc & nâng cấp ô tô tại Pleiku',
     'MT Auto: độ đèn bi LED, màn hình Android, phanh Brembo, mâm, ốp gầm, body kit và chăm sóc xe tại 71A Tôn Thất Tùng, Pleiku. Hotline 0823 418 418.',
     home, nextp('dich-vu.html', 'Dịch vụ'))

# ----------------------------------------------------------------- SERVICES
hrows = ''.join(f'''
    <a class="hrow" href="#{sid}"><span class="mono">({num})</span><h3>{title}</h3><p>{desc}</p><span class="go">→</span></a>'''
    for sid, num, en, title, svc, desc, items, pic, _ in SERVICES)
hfloat = ''.join(f'<img src="assets/img/{pic}.jpg" alt="">' for *_, pic, _x in SERVICES)
snav = ''.join(f'<a href="#{sid}"><i></i>{plain(svc)}</a>' for sid, num, en, title, svc, *_ in SERVICES)
sblocks = ''.join(f'''
      <article class="sblock" id="{sid}">
        <div class="sblock-media" data-img>{im(detail, plain(title), ' data-speed="0.1"')}</div>
        <div>
          <span class="mono" data-fade>({num}) {en}</span>
          <h2 data-split>{title}</h2>
          <p data-fade>{desc}</p>
          <ul data-fade>{''.join(f'<li>{it}</li>' for it in items)}</ul>
          <div data-fade>{btn('Đặt lịch dịch vụ', 'lien-he.html#booking', f' data-service="{plain(svc)}"')}</div>
        </div>
      </article>''' for sid, num, en, title, svc, desc, items, pic, detail in SERVICES)

services = phero('Dịch vụ — Services', 'Dịch vụ', 'Dịch vụ <span class="accent">tại MT Auto.</span>',
                 'Bốn nhóm dịch vụ chính — từ đồ chơi nâng cấp đến chăm sóc định kỳ — cùng một tiêu chuẩn: hàng chính hãng, tư vấn đúng xe, lắp đặt chỉn chu.',
                 ('team-work', 'Đội thợ MT Auto đang làm việc', 'center 80%')) + f'''

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
      <div class="faq-item open"><button class="faq-q" aria-expanded="true">Tôi có cần đặt lịch trước không?<i></i></button><div class="faq-a"><div><p>Nên đặt lịch trước để MT Auto chuẩn bị sẵn sản phẩm và sắp xếp thời gian cho xe của bạn. Bạn có thể gọi hotline {PHONE_TXT}, nhắn Zalo hoặc Messenger.</p></div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Chi phí được tính như thế nào?<i></i></button><div class="faq-a"><div><p>Chi phí phụ thuộc vào dòng xe, sản phẩm và hạng mục bạn chọn. MT Auto tư vấn và báo giá rõ ràng trước khi bắt đầu làm.</p></div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Lắp đặt mất bao lâu?<i></i></button><div class="faq-a"><div><p>Mỗi hạng mục có thời gian khác nhau. Thời gian dự kiến sẽ được báo cụ thể khi tư vấn để bạn chủ động sắp xếp.</p></div></div></div>
      <div class="faq-item"><button class="faq-q" aria-expanded="false">Tôi chưa biết nên nâng cấp gì cho xe?<i></i></button><div class="faq-a"><div><p>Bạn chỉ cần cho biết dòng xe và điều bạn muốn cải thiện — sáng hơn, tiện nghi hơn hay thể thao hơn. MT Auto sẽ gợi ý phương án phù hợp với nhu cầu và ngân sách.</p></div></div></div>
    </div>
  </div>
</section>'''
page('dich-vu.html', 'Dịch vụ — MT Auto Pleiku',
     'Độ đèn bi LED, màn hình Android & âm thanh, phanh – mâm – ốp gầm – body kit, chăm sóc & nội thất ô tô tại MT Auto Pleiku.',
     services, nextp('cong-trinh.html', 'Công trình'))

# ----------------------------------------------------------------- WORKS
WORKS = [
    ('do-den', 'shop-xpander', 'Độ bi X-Light V12 — Xpander', 'wide'),
    ('do-den', 'den-c3pro', 'Bi LED Steelmate C3-Pro', ''),
    ('man-hinh', 'man-d14', 'Android box D14 Ultra — Ford', ''),
    ('phanh-mam', 'phanh-brembo', 'Bộ phanh Brembo', ''),
    ('cham-soc', 'vo-lang-carbon', 'Vô lăng carbon — Kia', ''),
    ('phanh-mam', 'mam-do', 'Mâm thể thao &amp; heo Brembo', ''),
    ('do-den', 'xlight-cover', 'Độ bi X-Light V20', 'wide'),
    ('man-hinh', 'loa-steelmate', 'Loa sub Steelmate', ''),
    ('phanh-mam', 'gam-vinfast', 'Ốp gầm B-F — VinFast', 'wide'),
    ('do-den', 'den-gam', 'Đèn gầm sau khi lắp', ''),
    ('cham-soc', 'cs-phu-kinh', 'Phủ kính Meguiar’s', ''),
    ('man-hinh', 'man-icar', 'Màn hình iCar Elliview — Toyota', ''),
    ('phanh-mam', 'phanh-amg', 'Heo phanh AMG', 'wide'),
    ('cham-soc', 'noi-that-da', 'Bọc da bệ tì tay', ''),
    ('man-hinh', 'cam-70mai', 'Camera hành trình 70mai A200', ''),
    ('do-den', 'den-steelmate', 'Cặp bi Steelmate', ''),
    ('cham-soc', 'cs-nhot', 'Thay dầu nhớt — Toyota', ''),
    ('phanh-mam', 'gam-bf', 'Ốp gầm B-F', ''),
    ('man-hinh', 'man-d14-mazda', 'D14 Ultra — Mazda', ''),
    ('do-den', 'den-xlight-ford', 'Độ bi X-Light — Ford', 'wide'),
    ('cham-soc', 'noi-that-ni', 'Bọc nỉ bệ tì tay', ''),
    ('phanh-mam', 'phanh-lap', 'Lắp heo phanh', ''),
    ('man-hinh', 'man-gotech', 'Màn hình Gotech', ''),
    ('cham-soc', 'cs-bosch', 'Gạt mưa Bosch', ''),
    ('do-den', 'den-thao', 'Tháo đèn, chuẩn bị độ bi', ''),
    ('cham-soc', 'team-work', 'Đội thợ MT Auto', 'wide'),
    ('man-hinh', 'man-zestech', 'Màn hình Android', ''),
    ('phanh-mam', 'mam-brembo-set', 'Mâm, heo phanh &amp; ốc Rays', ''),
    ('cham-soc', 'vo-lang-kia', 'Khoang lái sau nâng cấp', ''),
]
CAT = {sid: plain(svc) for sid, num, en, title, svc, *_ in SERVICES}
works = ''.join(f'''
    <figure class="work {wide}" data-cat="{cat}" data-title="{plain(t)}" tabindex="0" data-cursor="view" data-fade style="--d:{(i % 3) * .08:.2f}s">{im(n, plain(t))}<figcaption><b>{t}</b><span class="mono">{CAT[cat]}</span></figcaption></figure>'''
    for i, (cat, n, t, wide) in enumerate(WORKS))
filters = ''.join(f'\n    <button data-filter="{sid}">{plain(svc)}</button>' for sid, num, en, title, svc, *_ in SERVICES)

works_page = phero('Công trình — Works', 'Công trình', 'Công trình <span class="accent">thực tế.</span>',
                   'Hình ảnh và video thật từ xưởng MT Auto — những chiếc xe đã được nâng cấp và chăm sóc tại 71A Tôn Thất Tùng, Pleiku.') + f'''

<section class="sec wrap" style="padding-top:clamp(60px,10vh,110px)">
  <div class="filters" role="group" aria-label="Lọc theo dịch vụ">
    <button class="on" data-filter="all">Tất cả</button>{filters}
  </div>
  <div class="works">{works}
  </div>
</section>
''' + reels('Video') + '''

<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Xem ảnh">
  <figure><img alt=""><figcaption><span class="cap"></span><span class="num mono"></span></figcaption></figure>
  <button class="x" aria-label="Đóng">✕</button>
  <button class="prev" aria-label="Ảnh trước">←</button>
  <button class="next" aria-label="Ảnh sau">→</button>
</div>''' + VPLAYER
page('cong-trinh.html', 'Công trình — MT Auto Pleiku',
     'Hình ảnh và video thực tế các công trình độ đèn, màn hình, phanh, mâm, body kit và chăm sóc xe tại MT Auto Pleiku.',
     works_page, nextp('lien-he.html', 'Liên hệ'))

# ----------------------------------------------------------------- CONTACT
chips = ''.join(f'\n          <label class="chip"><input type="radio" name="service" value="{plain(svc)}"{" checked" if i == 0 else ""}><span>{svc}</span></label>'
                for i, (sid, num, en, title, svc, *_) in enumerate(SERVICES))
contact = phero('Liên hệ — Contact', 'Liên hệ', 'Ghé thăm <span class="accent">MT Auto.</span>',
                'Gọi điện, nhắn tin hoặc để lại thông tin — MT Auto sẽ liên hệ lại để tư vấn cho chiếc xe của bạn.',
                ('storefront-wide', 'Mặt tiền xưởng MT Auto')) + f'''

<section class="sec wrap" style="padding-top:clamp(60px,10vh,110px)">
  <div class="cards">
    <a class="ccard" href="tel:{PHONE}" data-fade><span class="mono">Hotline</span><b>{PHONE_TXT}</b><span class="go">→</span></a>
    <a class="ccard" href="{ZALO}" target="_blank" rel="noopener" data-fade style="--d:.08s"><span class="mono">Zalo</span><b>Chat Zalo<br>{PHONE_TXT}</b><span class="go">→</span></a>
    <a class="ccard" href="{FB}" target="_blank" rel="noopener" data-fade style="--d:.16s"><span class="mono">Facebook</span><b>/mt.autochamsocxe</b><span class="go">→</span></a>
    <a class="ccard wide" href="{MAP_DIR}" target="_blank" rel="noopener" data-fade><span class="mono">Địa chỉ xưởng · 7:15 – 18:00</span><b>71A Tôn Thất Tùng,<br>Phường Pleiku, Gia Lai</b><span class="go">→</span></a>
  </div>
</section>

<section class="contact wrap" id="booking">
  <span class="label" data-fade>Đặt lịch hẹn</span>
  <h2 class="cta-big" style="font-size:clamp(52px,9vw,170px)"><span data-split>Để lại thông tin,</span><br><span data-split style="--d:.1s">MT gọi lại ngay.</span></h2>
  <div class="contact-grid">
    <div class="contact-info" data-fade>
      <div><span class="mono">Hotline</span><a class="big ulink" href="tel:{PHONE}">{PHONE_TXT}</a></div>
      <div><span class="mono">Email</span><a class="big ulink" href="mailto:{EMAIL}" style="word-break:break-all">{EMAIL}</a></div>
      <div><span class="mono">Phản hồi</span><p style="color:rgba(247,246,243,.7);max-width:340px">MT Auto sẽ liên hệ lại để tư vấn chi tiết cho chiếc xe của bạn.</p></div>
    </div>
    <form class="form" id="booking-form" data-fade style="--d:.1s" novalidate>
      <div class="field full"><label>Dịch vụ quan tâm</label>
        <div class="chips" role="radiogroup" aria-label="Dịch vụ quan tâm">{chips}
          <label class="chip"><input type="radio" name="service" value="Khác"><span>Khác</span></label>
        </div>
      </div>
      <div class="field"><label for="f-name">Họ và tên</label><input id="f-name" name="name" placeholder="Nguyễn Văn A" autocomplete="name"></div>
      <div class="field"><label for="f-phone">Số điện thoại</label><input id="f-phone" name="phone" type="tel" placeholder="09xx xxx xxx" autocomplete="tel"></div>
      <div class="field full"><label for="f-car">Dòng xe</label><input id="f-car" name="car" placeholder="Ví dụ: Mazda CX-5 2022"></div>
      <div class="field full"><label for="f-msg">Lời nhắn</label><textarea id="f-msg" name="message" rows="2" placeholder="Mô tả ngắn nhu cầu của bạn"></textarea></div>
      <div class="form-foot">
        <small id="formNote">Nút gửi sẽ mở ứng dụng email của bạn với nội dung đã điền sẵn.</small>
        <button class="btn light" type="submit"><span class="btn-roll"><span data-t="Gửi yêu cầu">Gửi yêu cầu</span></span><span class="btn-ico"><i>→</i><i>→</i></span></button>
      </div>
    </form>
  </div>
</section>
''' + visit('map')
page('lien-he.html', 'Liên hệ — MT Auto Pleiku',
     'Liên hệ MT Auto: 71A Tôn Thất Tùng, Phường Pleiku, Gia Lai. Hotline / Zalo 0823 418 418. Mở cửa 7:15 – 18:00.',
     contact, nextp('index.html', 'Trang chủ'))
# ----------------------------------------------------------------- SEO files
import datetime
today = datetime.date.today().isoformat()
urls = ''.join(f'  <url><loc>{SITE_URL}{"" if f == "index.html" else f}</loc><lastmod>{today}</lastmod><priority>{"1.0" if f == "index.html" else "0.8"}</priority></url>\n' for f, _ in PAGES)
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8').write(f'User-agent: *\nAllow: /\nDisallow: /wordpress-cu/\n\nSitemap: {SITE_URL}sitemap.xml\n')
print('ok')
