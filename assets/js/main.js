/* =====================================================================
   MT AUTO CARE — shared site script
   Loader, page transitions, smooth scroll and every scroll scene.
   Each feature checks for its own markup, so one file serves all pages.
   ===================================================================== */
(() => {
'use strict';
const $ = (s, c = document) => c.querySelector(s);
const $$ = (s, c = document) => [...c.querySelectorAll(s)];
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const lerp = (a, b, t) => a + (b - a) * t;
const range = (v, a, b) => clamp((v - a) / (b - a));
const easeOut = t => 1 - Math.pow(1 - t, 3);
const easeInOut = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
const store = {
  get: k => { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
  set: (k, v) => { try { sessionStorage.setItem(k, v); } catch (e) {} },
  del: k => { try { sessionStorage.removeItem(k); } catch (e) {} }
};

const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
const html = document.documentElement, body = document.body;
let vw = innerWidth, vh = innerHeight;
if ('scrollRestoration' in history) history.scrollRestoration = 'manual';

const safe = fn => { try { fn(); } catch (e) { console.error('[mt]', e); } };
let last = -1;          // last painted scroll position (used by measure + frame)
const onScroll = [];   // fn(y) — runs when scroll position changes
const onMeasure = [];  // fn()  — runs on load/resize
const offTop = el => { const r = el.getBoundingClientRect(); return { top: r.top + scrollY, h: r.height }; };
const maxScroll = () => document.documentElement.scrollHeight - innerHeight;

/* ---------- logo / image fallbacks ---------- */
$$('.brand img').forEach(img => {
  const fail = () => img.parentElement.classList.add('nologo');
  img.addEventListener('error', fail);
  if (img.complete && img.naturalWidth === 0) fail();
});
$$('img[data-fallback]').forEach(img => {
  const swap = () => { if (img.dataset.fallback) { img.src = img.dataset.fallback; img.removeAttribute('data-fallback'); } };
  img.addEventListener('error', swap);
  if (img.complete && img.naturalWidth === 0) swap();
});

/* ---------- word splitting (keeps nested markup) ---------- */
function splitWords(root) {
  let i = 0;
  const walk = node => {
    [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(p => {
          if (!p) return;
          if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(' ')); return; }
          const w = document.createElement('span'); w.className = 'wd'; w.setAttribute('aria-hidden', 'true');
          const inner = document.createElement('span'); inner.textContent = p; inner.style.setProperty('--i', i++);
          w.appendChild(inner); frag.appendChild(w);
        });
        n.replaceWith(frag);
      } else if (n.nodeType === 1 && n.tagName !== 'BR' && n.tagName !== 'SMALL') walk(n);
    });
  };
  walk(root);
}
$$('[data-split],[data-split-now]').forEach(el => {
  el.setAttribute('aria-label', el.textContent.replace(/\s+/g, ' ').trim());
  splitWords(el);
  if (el.hasAttribute('data-split-now')) el.setAttribute('data-split', '');
});

/* ---------- page transition + loader ---------- */
const pt = $('#pt');
const loader = $('#loader');
const arrived = html.classList.contains('pt-arrive');
let started = false;

function start() {
  if (started) return; started = true;
  if (location.hash && $(location.hash)) {
    const t = $(location.hash);
    window.scrollTo(0, t.getBoundingClientRect().top + scrollY);
  } else window.scrollTo(0, 0);
  body.classList.add('loaded'); body.classList.remove('is-loading');
  measure();
}

if (arrived && pt) {
  // came from another page: the curtain is already covering — lift it
  store.del('mt-pt');
  body.classList.add('loader-done');
  pt.classList.add('cover');
  html.classList.remove('pt-arrive');
  const lift = () => requestAnimationFrame(() => {
    void pt.offsetWidth;
    pt.classList.remove('cover'); pt.classList.add('in');
    start();
    setTimeout(() => pt.classList.remove('in'), 1100);
  });
  (document.fonts ? Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 400))]) : Promise.resolve()).then(lift);
} else if (loader && !reduced) {
  const num = $('#loaderNum'), line = $('#loaderLine');
  const pre = $$('img[data-preload]');
  const seen = store.get('mt-seen') === '1';
  const minT = seen ? 700 : 1900;
  let got = 0, shown = 0;
  const need = pre.length + 1, t0 = performance.now();
  const hit = () => got++;
  pre.forEach(img => img.complete ? hit() : (img.addEventListener('load', hit, { once: true }), img.addEventListener('error', hit, { once: true })));
  (document.fonts ? document.fonts.ready : Promise.resolve()).then(hit);
  const tickL = now => {
    const el = now - t0;
    const target = Math.min(got / need, clamp(el / minT)) * 100;
    shown = el > 5500 ? lerp(shown, 100, .15) : lerp(shown, target, seen ? .14 : .075);
    if (target >= 100 && shown > 99.5) shown = 100;
    if (num) num.textContent = Math.round(shown);
    if (line) line.style.transform = `scaleX(${shown / 100})`;
    if (shown >= 100 || (el > 5500 && shown > 99.5)) {
      if (num) num.textContent = '100';
      store.set('mt-seen', '1');
      setTimeout(() => { start(); setTimeout(() => body.classList.add('loader-done'), 1400); }, 250);
      return;
    }
    requestAnimationFrame(tickL);
  };
  requestAnimationFrame(tickL);
} else { body.classList.add('loader-done'); start(); }

// back/forward cache: never come back to a covered page
addEventListener('pageshow', e => { if (e.persisted && pt) { pt.className = 'pt'; body.classList.add('loaded', 'loader-done'); body.classList.remove('is-loading'); } });

function leaveTo(href) {
  if (!pt || reduced) { location.href = href; return; }
  store.set('mt-pt', '1');
  pt.classList.remove('in', 'cover'); void pt.offsetWidth;
  pt.classList.add('out');
  setTimeout(() => { location.href = href; }, 850);
}

/* ---------- smooth wheel scroll ---------- */
const sm = { on: fine && !reduced, active: false, target: 0, cur: 0, k: .1 };
if (sm.on) {
  addEventListener('wheel', e => {
    if (e.ctrlKey) return;
    if (body.classList.contains('is-loading') || (pt && pt.classList.contains('out'))) { e.preventDefault(); return; }
    if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
    if (e.target.closest && e.target.closest('textarea, .lb, .vp')) return;
    if (body.classList.contains('menu-open')) return;
    e.preventDefault();
    let d = e.deltaY; if (e.deltaMode === 1) d *= 40; else if (e.deltaMode === 2) d *= innerHeight;
    if (!sm.active) sm.cur = sm.target = scrollY;
    sm.target = clamp(sm.target + d, 0, maxScroll()); sm.k = .1; sm.active = true;
  }, { passive: false });
  addEventListener('scroll', () => { if (!sm.active) sm.cur = sm.target = scrollY; }, { passive: true });
  addEventListener('keydown', () => { sm.active = false; });
  addEventListener('mousedown', e => { if (e.target === document.documentElement) sm.active = false; });
}
function scrollToY(y) {
  y = clamp(y, 0, maxScroll());
  if (sm.on) { if (!sm.active) sm.cur = scrollY; sm.target = y; sm.k = .07; sm.active = true; }
  else window.scrollTo({ top: y, behavior: reduced ? 'auto' : 'smooth' });
}

/* ---------- menu ---------- */
const menuBtn = $('#menuBtn');
const setMenu = open => {
  body.classList.toggle('menu-open', open);
  if (menuBtn) { menuBtn.setAttribute('aria-expanded', open); menuBtn.textContent = open ? 'Đóng' : 'Menu'; }
};
if (menuBtn) menuBtn.addEventListener('click', () => setMenu(!body.classList.contains('menu-open')));
addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });

/* ---------- links: in-page anchors scroll, other pages transition ---------- */
const herePath = location.pathname.replace(/\/$/, '/index.html');
document.addEventListener('click', e => {
  const a = e.target.closest && e.target.closest('a[href]');
  if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
  if (a.target === '_blank' || a.hasAttribute('download')) return;
  const raw = a.getAttribute('href');
  if (/^(tel:|mailto:|sms:|javascript:)/i.test(raw)) return;
  if (a.dataset.service) store.set('mt-service', a.dataset.service);
  const url = new URL(a.href, location.href);
  if (url.protocol !== location.protocol || url.host !== location.host) return;
  const samePage = url.pathname.replace(/\/$/, '/index.html') === herePath;
  if (samePage) {
    e.preventDefault(); setMenu(false);
    const el = url.hash.length > 1 && $(url.hash);
    if (url.hash === '#top' || !url.hash) scrollToY(0);
    else if (el) scrollToY(el.getBoundingClientRect().top + scrollY);
    pickService();
    return;
  }
  e.preventDefault(); setMenu(false);
  leaveTo(url.href);
});

/* ---------- reveals ---------- */
const revealEls = $$('[data-split]:not([data-split-now]),[data-fade],[data-img],#footMark');
// reduced motion still gets reveals — CSS turns them into plain fades
if ('IntersectionObserver' in window) {
  const map = new Map();
  const io = new IntersectionObserver(es => es.forEach(en => {
    if (!en.isIntersecting) return;
    (map.get(en.target) || []).forEach(el => el.classList.add('in'));
    io.unobserve(en.target);
  }), { threshold: .12, rootMargin: '0px 0px -5% 0px' });
  revealEls.forEach(el => {
    const w = el.hasAttribute('data-img') ? el.parentElement : el; // fully clipped boxes never report intersection
    if (!map.has(w)) map.set(w, []);
    map.get(w).push(el); io.observe(w);
  });
} else revealEls.forEach(el => el.classList.add('in'));

/* ---------- header, progress bar, back-to-top ---------- */
safe(() => {
  const header = $('#header'), progress = $('#progress'), ring = $('#totopRing'), totop = $('#totop');
  let lastY = 0;
  if (totop) totop.addEventListener('click', () => scrollToY(0));
  onScroll.push(y => {
    const p = clamp(y / Math.max(1, maxScroll()));
    if (progress) progress.style.transform = `scaleX(${p})`;
    if (ring) ring.style.strokeDashoffset = (170 * (1 - p)).toFixed(1);
    if (header && !body.classList.contains('menu-open')) {
      if (y > lastY + 4 && y > vh * .5) header.classList.add('hide');
      else if (y < lastY - 4 || y < vh * .5) header.classList.remove('hide');
    }
    lastY = y;
  });
});

/* ---------- home hero: frame shrinks into a rounded card ---------- */
safe(() => {
  const frame = $('#heroFrame'), img = $('#heroImg'), content = $('#heroContent');
  if (frame) onScroll.push(y => {
    if (y > vh * 1.2) return;
    const p = clamp(y / vh);
    frame.style.transform = `scale(${1 - p * .08})`;
    frame.style.borderRadius = (p * 28).toFixed(1) + 'px';
    if (img) img.style.transform = `translate3d(0, ${y * .25}px, 0)`;
    if (content) { content.style.transform = `translate3d(0, ${y * -.18}px, 0)`; content.style.opacity = clamp(1 - p * 1.4).toFixed(3); }
  });
});

/* ---------- words that light up while reading ---------- */
safe(() => $$('[data-scrub]').forEach(el => {
  let hot = false;  // words between *...* are highlighted
  el.innerHTML = el.textContent.trim().split(/\s+/).map(w => {
    if (w.startsWith('*')) hot = true;
    const html = `<span class="w${hot ? ' hot' : ''}">${w.replace(/\*/g, '')}</span>`;
    if (/\*[.,]?$/.test(w)) hot = false;
    return html;
  }).join(' ');
  const words = $$('.w', el); let m = { top: 0, h: 0 };
  onMeasure.push(() => { m = offTop(el); });
  onScroll.push(y => {
    const p = range(y + vh, m.top + vh * .15, m.top + m.h + vh * .4);
    const lit = Math.floor(p * words.length * 1.05);
    words.forEach((w, i) => w.classList.toggle('on', i < lit));
  });
}));

/* ---------- parallax images ---------- */
safe(() => {
  const imgs = $$('img[data-speed]'); let ms = [];
  onMeasure.push(() => { ms = imgs.map(i => offTop(i.parentElement)); });
  if (imgs.length) onScroll.push(y => imgs.forEach((img, i) => {
    const m = ms[i]; if (!m || y + vh < m.top || y > m.top + m.h) return;
    const c = (m.top + m.h / 2 - (y + vh / 2)) / vh;
    img.style.transform = `translate3d(0, ${(c * parseFloat(img.dataset.speed) * 100).toFixed(2)}%, 0)`;
  }));
});

/* ---------- stacked cards ---------- */
safe(() => {
  const cards = $$('.card'), shades = cards.map(c => $('.card-shade', c)); let tops = [];
  onMeasure.push(() => { tops = cards.map(c => parseFloat(getComputedStyle(c).top) || 0); });
  if (cards.length > 1) onScroll.push(() => {
    for (let i = 0; i < cards.length - 1; i++) {
      const nextTop = cards[i + 1].getBoundingClientRect().top, stick = tops[i + 1] || 0;
      const p = clamp(1 - (nextTop - stick) / Math.max(1, vh - stick));
      cards[i].style.transform = `scale(${(1 - p * .07).toFixed(4)})`;
      if (shades[i]) shades[i].style.opacity = (p * .55).toFixed(3);
    }
  });
});

/* ---------- zoom-through ---------- */
safe(() => {
  const zoom = $('#zoom'), st = $('#zoomStick'), pct = $('#zoomPct'); let m = { top: 0, h: 0 };
  if (zoom && st) {
    onMeasure.push(() => { m = offTop(zoom); });
    onScroll.push(y => {
      if (y < m.top - vh || y > m.top + m.h) return;
      const t = range(y, m.top, m.top + m.h - vh);
      const e = easeInOut(range(t, .05, .6));
      const sx = vw > 640 ? .34 : .14, sy = vw > 640 ? .28 : .3;
      st.style.setProperty('--zx', ((1 - e) * sx * vw).toFixed(1) + 'px');
      st.style.setProperty('--zy', ((1 - e) * sy * vh).toFixed(1) + 'px');
      st.style.setProperty('--zr', ((1 - e) * 18).toFixed(1) + 'px');
      st.style.setProperty('--zs', (1.4 - e * .4).toFixed(4));
      st.style.setProperty('--zw', (e * vw * .6).toFixed(1) + 'px');
      st.style.setProperty('--zc', easeOut(range(t, .62, .85)).toFixed(3));
      if (pct) pct.textContent = String(Math.round(e * 100)).padStart(3, '0') + '%';
    });
  }
});

/* ---------- process steps ---------- */
safe(() => {
  const steps = $$('.pstep'), count = $('#pcount'); let ms = [], cur = -1;
  const set = i => { if (i === cur) return; cur = i; steps.forEach((s, j) => s.classList.toggle('on', j === i)); if (count) count.style.transform = `translateY(${-i * 25}%)`; };
  if (steps.length) {
    set(0);
    onMeasure.push(() => { ms = steps.map(offTop); });
    onScroll.push(y => {
      if (vw <= 1000) return;
      let best = 0, bd = Infinity;
      ms.forEach((s, i) => { const d = Math.abs(s.top + s.h * .35 - (y + vh * .5)); if (d < bd) { bd = d; best = i; } });
      set(best);
    });
  }
});

/* ---------- drifting gallery rows ---------- */
safe(() => {
  const gal = $('#gallery'), rows = $$('.grow'); let m = { top: 0, h: 0 }, widths = [];
  if (gal && rows.length) {
    onMeasure.push(() => { m = offTop(gal); widths = rows.map(r => r.scrollWidth); });
    onScroll.push(y => {
      if (y + vh < m.top || y > m.top + m.h) return;
      const p = range(y + vh, m.top, m.top + m.h + vh);
      rows.forEach((r, i) => {
        const d = Math.max(0, widths[i] - vw) * .7;
        r.style.transform = `translate3d(${(-(i % 2 ? 1 - p : p) * d).toFixed(1)}px,0,0)`;
      });
    });
  }
});

/* ---------- faq ---------- */
$$('.faq-q').forEach(q => q.addEventListener('click', () => {
  const item = q.parentElement, open = !item.classList.contains('open');
  $$('.faq-item').forEach(it => { it.classList.remove('open'); $('.faq-q', it).setAttribute('aria-expanded', 'false'); });
  item.classList.toggle('open', open); q.setAttribute('aria-expanded', open);
  setTimeout(measure, 750);
}));

/* ---------- cursor ---------- */
const cursor = $('#cursor'), cdot = cursor && $('.cursor-dot', cursor);
const mouse = { x: -100, y: -100 }, cpos = { x: -100, y: -100 };
if (cursor && fine && !reduced) safe(() => {
  html.classList.add('has-cursor');
  addEventListener('mousemove', e => { mouse.x = e.clientX; mouse.y = e.clientY; cursor.classList.remove('off'); }, { passive: true });
  document.addEventListener('mouseleave', () => cursor.classList.add('off'));
  document.addEventListener('mouseover', e => {
    const t = e.target.closest && e.target.closest('a, button, label, input, textarea, [data-cursor], .ba');
    const view = !!(t && t.closest('[data-cursor="view"]'));
    cursor.classList.toggle('view', view);
    cursor.classList.toggle('hover', !!t && !view);
    const lbl = $('span', cdot); if (lbl) lbl.textContent = ((t && t.closest('[data-cursor-label]')) || {dataset:{}}).dataset.cursorLabel || 'Xem';
  });
});

/* ---------- ticker ---------- */
const ticker = $('#ticker'), tg = ticker && $('.ticker-group', ticker);
let tx = 0, tw = 0, tdir = -1;
if (ticker) { for (let i = 0; i < 3; i++) ticker.appendChild(tg.cloneNode(true)); onMeasure.push(() => { tw = tg.getBoundingClientRect().width; }); }

/* ---------- clock ---------- */
safe(() => {
  const clock = $('#clock');
  const tick = () => { try { clock.textContent = 'VN ' + new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit', timeZone: 'Asia/Ho_Chi_Minh' }); } catch (e) { clock.textContent = ''; } };
  if (clock) { tick(); setInterval(tick, 30000); }
});

/* ---------- footer wordmark ---------- */
safe(() => {
  const fm = $('#footMark');
  if (fm) {
    fm.innerHTML = [...fm.textContent].map((c, i) => `<span aria-hidden="true" class="${i < 2 ? 'r' : i >= 3 && i <= 6 ? 'a' : ''}" style="--i:${i}">${c === ' ' ? '&nbsp;' : c}</span>`).join('');
    onMeasure.push(() => {
      fm.style.fontSize = '100px';
      const ch = fm.children, w = ch[ch.length - 1].getBoundingClientRect().right - ch[0].getBoundingClientRect().left;
      fm.style.fontSize = Math.floor(Math.min(100 * fm.clientWidth / w * .985, Math.max(40, vw * .09))) + 'px';
    });
  }
});

/* ---------- hover index: image follows the cursor ---------- */
safe(() => {
  const idx = $('.hindex'), float = $('.hfloat');
  if (idx && float && fine && !reduced) {
    const imgs = $$('img', float); const pos = { x: 0, y: 0 }, cur = { x: 0, y: 0 }; let on = false;
    $$('.hrow', idx).forEach((row, i) => {
      row.addEventListener('mouseenter', () => { on = true; float.classList.add('on'); imgs.forEach((im, j) => im.classList.toggle('on', j === i)); });
    });
    idx.addEventListener('mouseleave', () => { on = false; float.classList.remove('on'); });
    idx.addEventListener('mousemove', e => { pos.x = e.clientX; pos.y = e.clientY; });
    const loop = () => {
      cur.x = lerp(cur.x, pos.x, .12); cur.y = lerp(cur.y, pos.y, .12);
      const rot = clamp((pos.x - cur.x) * .08, -10, 10);
      float.style.transform = `translate3d(${cur.x - 150}px, ${cur.y - 190}px, 0) rotate(${rot}deg)`;
      requestAnimationFrame(loop);
    };
    loop();
  }
});

/* ---------- service page: sticky nav follows the block in view ---------- */
safe(() => {
  const links = $$('.snav a'), blocks = links.map(a => $(a.getAttribute('href'))).filter(Boolean); let ms = [];
  if (blocks.length) {
    onMeasure.push(() => { ms = blocks.map(offTop); });
    onScroll.push(y => {
      let best = 0;
      ms.forEach((m, i) => { if (y + vh * .4 >= m.top) best = i; });
      links.forEach((a, i) => a.classList.toggle('on', i === best));
    });
  }
});

/* ---------- works: filter + lightbox ---------- */
safe(() => {
  const works = $$('.work'), lb = $('#lb');
  $$('.filters button').forEach(b => b.addEventListener('click', () => {
    $$('.filters button').forEach(x => x.classList.toggle('on', x === b));
    const f = b.dataset.filter;
    works.forEach(w => {
      const show = f === 'all' || w.dataset.cat === f;
      if (show && w.classList.contains('hide')) {
        w.classList.remove('hide'); w.style.opacity = 0; w.style.transform = 'translateY(30px)';
        requestAnimationFrame(() => requestAnimationFrame(() => { w.style.opacity = ''; w.style.transform = ''; }));
      } else if (!show) w.classList.add('hide');
    });
    setTimeout(measure, 50);
  }));
  if (lb && works.length) {
    const img = $('img', lb), cap = $('.cap', lb), num = $('.num', lb);
    let list = [], at = 0;
    const show = i => {
      at = (i + list.length) % list.length; const w = list[at], src = $('img', w);
      img.src = src.currentSrc || src.src; img.alt = src.alt;
      cap.textContent = w.dataset.title || src.alt; num.textContent = `${at + 1} / ${list.length}`;
    };
    const open = w => { list = works.filter(x => !x.classList.contains('hide')); show(list.indexOf(w)); lb.classList.add('open'); body.style.overflow = 'hidden'; $('.x', lb).focus(); };
    const close = () => { lb.classList.remove('open'); body.style.overflow = ''; };
    works.forEach(w => {
      w.addEventListener('click', () => open(w));
      w.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(w); } });
    });
    $('.x', lb).addEventListener('click', close);
    $('.prev', lb).addEventListener('click', () => show(at - 1));
    $('.next', lb).addEventListener('click', () => show(at + 1));
    lb.addEventListener('click', e => { if (e.target === lb) close(); });
    addEventListener('keydown', e => {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close(); else if (e.key === 'ArrowLeft') show(at - 1); else if (e.key === 'ArrowRight') show(at + 1);
    });
  }
});

/* ---------- before / after slider ---------- */
$$('.ba').forEach(ba => {
  let drag = false;
  const set = x => { const r = ba.getBoundingClientRect(); ba.style.setProperty('--p', (clamp((x - r.left) / r.width) * 100).toFixed(2) + '%'); };
  ba.addEventListener('pointerdown', e => { drag = true; ba.setPointerCapture(e.pointerId); set(e.clientX); });
  ba.addEventListener('pointermove', e => { if (drag) set(e.clientX); });
  ba.addEventListener('pointerup', () => { drag = false; });
  ba.addEventListener('pointercancel', () => { drag = false; });
  ba.tabIndex = 0;
  ba.addEventListener('keydown', e => {
    const p = parseFloat(getComputedStyle(ba).getPropertyValue('--p')) || 50;
    if (e.key === 'ArrowLeft') ba.style.setProperty('--p', clamp(p - 5, 0, 100) + '%');
    if (e.key === 'ArrowRight') ba.style.setProperty('--p', clamp(p + 5, 0, 100) + '%');
  });
});

/* ---------- videos: mobile hero loop, reel previews, full player ---------- */
safe(() => {
  const probe = document.createElement('video');
  const VEXT = probe.canPlayType('video/webm; codecs="vp9"') ? 'webm' : 'mp4';
  const vsrc = u => u.replace(/\.mp4$/, '.' + VEXT);
  // phones: full-screen portrait loop; desktops: blurred backdrop + sharp portrait panel
  const heroVids = matchMedia('(max-width: 640px)').matches ? $$('.hero-video')
    : matchMedia('(min-width: 900px)').matches ? $$('.hero-dv video') : [];
  heroVids.forEach(v => { v.src = vsrc(v.dataset.src); v.play().catch(() => {}); });
  if (heroVids.length) {
    let heroPlaying = true;
    onScroll.push(y => {
      const show = y < vh * 1.2;
      if (show === heroPlaying) return;
      heroPlaying = show;
      heroVids.forEach(v => show ? v.play().catch(() => {}) : v.pause());
    });
  }
  const previews = $$('.reel-phone video');
  if (previews.length && 'IntersectionObserver' in window) {
    const vio = new IntersectionObserver(es => es.forEach(en => {
      const v = en.target;
      if (en.isIntersecting) { if (!v.getAttribute('src')) v.src = vsrc(v.dataset.src); v.play().catch(() => {}); }
      else v.pause();
    }), { threshold: .35 });
    previews.forEach(v => vio.observe(v));
  }
  const vp = $('#vp');
  if (vp) {
    const pv = $('video', vp);
    const close = () => { vp.classList.remove('open'); pv.pause(); body.style.overflow = ''; };
    $$('.reel-phone').forEach(b => b.addEventListener('click', () => {
      pv.src = vsrc(b.dataset.full); pv.poster = $('video', b).poster;
      vp.classList.add('open'); body.style.overflow = 'hidden';
      pv.play().catch(() => {});
      $('.x', vp).focus();
    }));
    $('.x', vp).addEventListener('click', close);
    vp.addEventListener('click', e => { if (e.target === vp) close(); });
    addEventListener('keydown', e => { if (e.key === 'Escape' && vp.classList.contains('open')) close(); });
  }
});

/* ---------- booking form ---------- */
function pickService() {
  const s = store.get('mt-service'); if (!s) return;
  const r = $$('input[name="service"]').find(x => x.value === s);
  if (r) { r.checked = true; store.del('mt-service'); }
}
pickService();
safe(() => {
  const form = $('#booking-form');
  if (form) form.addEventListener('submit', e => {
    e.preventDefault();
    const d = new FormData(form), note = $('#formNote');
    const name = (d.get('name') || '').trim(), phone = (d.get('phone') || '').trim();
    if (!name || !phone) {
      note.textContent = 'Vui lòng điền họ tên và số điện thoại để chúng tôi liên hệ lại.';
      note.style.color = 'var(--accent)'; (name ? $('#f-phone') : $('#f-name')).focus(); return;
    }
    const txt = `Họ tên: ${name}\nSố điện thoại: ${phone}\nDịch vụ: ${d.get('service')}\nDòng xe: ${d.get('car') || ''}\nLời nhắn: ${d.get('message') || ''}`;
    location.href = `mailto:lienhe@mtautocare.com?subject=${encodeURIComponent('Đặt lịch — MT Auto Care')}&body=${encodeURIComponent(txt)}`;
    note.textContent = 'Cảm ơn bạn! Ứng dụng email đang được mở để gửi yêu cầu.'; note.style.color = '';
  });
});
$$('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

/* ---------- measure + main loop ---------- */
function measure() { vw = innerWidth; vh = innerHeight; onMeasure.forEach(f => f()); last = -1; }
let prev = performance.now(), lastFrameY = 0;
function frame(now) {
  const dt = Math.min(64, now - prev) / 16.667; prev = now;
  if (sm.active) {
    sm.cur = lerp(sm.cur, sm.target, 1 - Math.pow(1 - sm.k, dt));
    if (Math.abs(sm.target - sm.cur) < .4) { sm.cur = sm.target; sm.active = false; }
    window.scrollTo(0, sm.cur);
  }
  const y = scrollY, vel = y - lastFrameY; lastFrameY = y;
  if (!reduced) {
    if (ticker) {
      if (vel) tdir = vel > 0 ? -1 : 1;
      tx += (tdir * .6 + tdir * Math.min(Math.abs(vel), 80) * .3) * dt;
      if (tw) { if (tx <= -tw) tx += tw; if (tx > 0) tx -= tw; }
      ticker.style.transform = `translate3d(${tx.toFixed(2)}px,0,0)`;
    }
    if (cdot && fine) {
      cpos.x = lerp(cpos.x, mouse.x, 1 - Math.pow(.8, dt)); cpos.y = lerp(cpos.y, mouse.y, 1 - Math.pow(.8, dt));
      cdot.style.transform = `translate3d(${cpos.x}px,${cpos.y}px,0)`;
    }
  }
  if (y !== last) {
    last = y;
    if (!reduced) onScroll.forEach(f => f(y));
    else onScroll[0] && onScroll[0](y);
  }
  requestAnimationFrame(frame);
}
let rt;
addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(measure, 120); }, { passive: true });
addEventListener('load', measure);
if (document.fonts) document.fonts.ready.then(measure);
measure();
requestAnimationFrame(frame);
})();
