/* =================================================================
   TeknoBlog — main.js
   ================================================================= */

(function () {
  'use strict';

  /* ---------- Tema ---------- */
  const STORAGE_KEY = 'teknoblog-theme';
  const toggle = document.querySelector('.theme-toggle');
  const html = document.documentElement;

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    if (toggle) toggle.textContent = theme === 'dark' ? '☀️' : '🌙';
  }

  setTheme(localStorage.getItem(STORAGE_KEY) || 'light');

  if (toggle) {
    toggle.addEventListener('click', function () {
      setTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
    });
  }

  /* ---------- Mobil Menü ---------- */
  const menuBtn = document.querySelector('.mobile-menu-btn');
  const nav = document.querySelector('nav');

  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      nav.classList.toggle('active');
      menuBtn.textContent = nav.classList.contains('active') ? '✕' : '☰';
    });
  }

  /* ---------- Aktif Sayfa ---------- */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('nav a').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ---------- Reklam Slotlari (AdSense Yerlesimi) ----------
     AdSense onayi oncesi KAPALI: bos "Reklam Alani" kutulari politika
     incelemesinde "reklam icin yapilmis site" izlenimi verir. Onay sonrasi
     gercek AdSense kodlari buraya eklenecek. */
  function insertAdSlots() {
    return;
  }

  /* ---------- Okuma Süresi ---------- */
  function calcReadTime() {
    var el = document.querySelector('.read-time');
    if (!el) return;
    var content = document.querySelector('.article-content');
    if (!content) return;
    var words = content.textContent.split(/\s+/).length;
    var mins = Math.ceil(words / 200);
    el.textContent = mins + ' dk okuma';
  }

  /* ---------- scroll ---------- */
  function onScroll() {
    var header = document.querySelector('.site-header');
    if (!header) return;
    if (window.scrollY > 50) {
      header.style.boxShadow = '0 2px 12px rgba(0,0,0,.06)';
    } else {
      header.style.boxShadow = 'none';
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- İletişim Formu ---------- */

  /* ---------- Arama ---------- */
  var inArticles = location.pathname.indexOf('/articles/') !== -1;
  var PATH = inArticles ? '../' : '';
  var indexData = null;
  var indexLoading = false;

  function normalize(s) {
    return (s || '').toLowerCase()
      .replace(/ı/g, 'i').replace(/İ/g, 'i').replace(/ş/g, 's')
      .replace(/ğ/g, 'g').replace(/ü/g, 'u').replace(/ö/g, 'o')
      .replace(/ç/g, 'c').replace(/â/g, 'a').replace(/î/g, 'i')
      .replace(/[^a-z0-9\s]/g, ' ').replace(/\s+/g, ' ').trim();
  }

  function loadIndex() {
    if (indexData || indexLoading) return Promise.resolve(indexData);
    indexLoading = true;
    return fetch(PATH + 'search-index.json')
      .then(function (r) { return r.json(); })
      .then(function (d) { indexData = d; indexLoading = false; return d; })
      .catch(function () { indexLoading = false; return null; });
  }

  function runSearch(q) {
    var nq = normalize(q);
    if (!nq || !indexData) return [];
    var words = nq.split(' ');
    var results = [];
    indexData.forEach(function (it) {
      var t = normalize(it.t), h = normalize(it.h), e = normalize(it.e),
          x = normalize(it.x), c = normalize(it.c);
      var score = 0, all = true;
      words.forEach(function (w) {
        var hit = false;
        if (t.indexOf(w) !== -1) { score += t.indexOf(w) === 0 ? 12 : 8; hit = true; }
        if (c.indexOf(w) !== -1) { score += 5; hit = true; }
        if (h.indexOf(w) !== -1) { score += 4; hit = true; }
        if (e.indexOf(w) !== -1) { score += 3; hit = true; }
        if (x.indexOf(w) !== -1) { score += 1; hit = true; }
        if (!hit) all = false;
      });
      if (all && score > 0) results.push({ it: it, score: score });
    });
    results.sort(function (a, b) { return b.score - a.score; });
    return results.slice(0, 10).map(function (r) { return r.it; });
  }

  function initSearch() {
    var header = document.querySelector('.header-inner');
    if (!header) return;

    var btn = document.createElement('button');
    btn.className = 'search-open-btn';
    btn.setAttribute('aria-label', 'Ara');
    btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg><span class="search-btn-text">Ara</span>';
    var menuBtn = header.querySelector('.mobile-menu-btn');
    header.insertBefore(btn, menuBtn || null);

    var box = document.createElement('div');
    box.className = 'search-overlay';
    box.innerHTML =
      '<div class="search-panel">' +
      '  <div class="search-input-wrap">' +
      '    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg>' +
      '    <input type="search" class="search-input" placeholder="Makalelerde ara... (Ctrl + K)" autocomplete="off">' +
      '    <button class="search-close" aria-label="Kapat">✕</button>' +
      '  </div>' +
      '  <div class="search-results"></div>' +
      '</div>';
    document.body.appendChild(box);

    var input = box.querySelector('.search-input');
    var resultsEl = box.querySelector('.search-results');

    function open() {
      box.classList.add('active');
      input.focus();
      loadIndex();
    }
    function close() {
      box.classList.remove('active');
      input.value = '';
      resultsEl.innerHTML = '';
    }

    btn.addEventListener('click', open);
    box.querySelector('.search-close').addEventListener('click', close);
    box.addEventListener('click', function (e) { if (e.target === box) close(); });

    input.addEventListener('input', function () {
      var q = input.value.trim();
      if (!q) { resultsEl.innerHTML = ''; return; }
      loadIndex().then(function () {
        var res = runSearch(q);
        if (!res.length) {
          resultsEl.innerHTML = '<div class="search-empty">Sonuç bulunamadı</div>';
          return;
        }
        resultsEl.innerHTML = res.map(function (it) {
          return '<a class="search-item" href="' + PATH + 'articles/' + it.s + '.html">' +
            '<span class="search-item-cat">' + it.c + '</span>' +
            '<span class="search-item-title">' + it.t + '</span>' +
            (it.e ? '<span class="search-item-ex">' + it.e + '</span>' : '') +
            '</a>';
        }).join('');
      });
    });

    document.addEventListener('keydown', function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        open();
      } else if (e.key === 'Escape') {
        close();
      }
    });
  }

  initSearch();

  /* ---------- Paylaş Butonları ---------- */
  function initShare() {
    var content = document.querySelector('.article-content');
    if (!content) return;

    var url = encodeURIComponent(location.href);
    var title = encodeURIComponent(document.title);
    var bar = document.createElement('div');
    bar.className = 'share-bar';
    bar.innerHTML =
      '<span class="share-label">Bu makaleyi paylaş:</span>' +
      '<a class="share-btn share-x" href="https://twitter.com/intent/tweet?url=' + url + '&text=' + title + '" target="_blank" rel="noopener">𝕏 Twitter</a>' +
      '<a class="share-btn share-wa" href="https://wa.me/?text=' + title + '%20' + url + '" target="_blank" rel="noopener">WhatsApp</a>' +
      '<a class="share-btn share-tg" href="https://t.me/share/url?url=' + url + '&text=' + title + '" target="_blank" rel="noopener">Telegram</a>' +
      '<a class="share-btn share-fb" href="https://www.facebook.com/sharer/sharer.php?u=' + url + '" target="_blank" rel="noopener">Facebook</a>' +
      '<button class="share-btn share-copy" type="button">🔗 Bağlantıyı kopyala</button>';

    var authorBox = content.querySelector('.author-box');
    if (authorBox) {
      content.insertBefore(bar, authorBox);
    } else {
      content.appendChild(bar);
    }

    var copyBtn = bar.querySelector('.share-copy');
    copyBtn.addEventListener('click', function () {
      var done = function () {
        copyBtn.textContent = '✅ Kopyalandı!';
        setTimeout(function () {
          copyBtn.innerHTML = '🔗 Bağlantıyı kopyala';
        }, 2000);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(location.href).then(done);
      } else {
        var ta = document.createElement('textarea');
        ta.value = location.href;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        done();
      }
    });
  }

  initShare();

  /* ---------- X Takip Butonu ---------- */
  function initFollowX() {
    var content = document.querySelector('.article-content');
    if (!content) return;
    var authorBox = content.querySelector('.author-box');
    if (!authorBox) return;

    var btn = document.createElement('div');
    btn.className = 'follow-x';
    btn.innerHTML =
      '<a href="https://x.com/blogTechWave" target="_blank" rel="noopener">' +
      '<span class="follow-x-logo">&#120143;</span>' +
      '<span class="follow-x-text"><strong>TechWave\'i X\'te takip et</strong>' +
      '<small>Günlük teknoloji ve yapay zeka içerikleri için @blogTechWave</small></span>' +
      '<span class="follow-x-cta">Takip et</span></a>';
    authorBox.parentNode.insertBefore(btn, authorBox.nextSibling);
  }

  initFollowX();

  /* ---------- Yorumlar (giscus) ---------- */
  function initComments() {
    var content = document.querySelector('.article-content');
    if (!content) return;

    var wrap = document.createElement('div');
    wrap.className = 'comments-box';
    wrap.innerHTML = '<h3 class="comments-title">💬 Yorumlar</h3><div class="giscus"></div>';
    content.appendChild(wrap);

    var s = document.createElement('script');
    s.src = 'https://giscus.app/client.js';
    s.setAttribute('data-repo', 'caglarc62/techwave-blog');
    s.setAttribute('data-repo-id', 'R_kgDOURcC4g');
    s.setAttribute('data-category', 'General');
    s.setAttribute('data-category-id', 'DIC_kwDOURcC4s4DGlkL');
    s.setAttribute('data-mapping', 'pathname');
    s.setAttribute('data-strict', '0');
    s.setAttribute('data-reactions-enabled', '1');
    s.setAttribute('data-emit-metadata', '0');
    s.setAttribute('data-input-position', 'bottom');
    s.setAttribute('data-theme', 'preferred_color_scheme');
    s.setAttribute('data-lang', 'tr');
    s.setAttribute('data-loading', 'lazy');
    s.crossOrigin = 'anonymous';
    s.async = true;
    wrap.appendChild(s);
  }

  initComments();

  /* ---------- Populer Makaleler (Metrica) ---------- */
  function initPopular() {
    var list = document.querySelector('.popular-list');
    if (!list) return;

    fetch(PATH + 'popular.json')
      .then(function (r) { return r.json(); })
      .then(function (items) {
        if (!items || !items.length) return;
        list.innerHTML = items.map(function (it, i) {
          return '<li><a href="' + PATH + 'articles/' + it.s + '.html">' +
            '<span class="popular-num">' + (i + 1) + '</span>' +
            '<span class="popular-body"><span class="popular-t">' + it.t + '</span>' +
            '<span class="popular-v">' + it.v + ' okuma</span></span></a></li>';
        }).join('');
      })
      .catch(function () {});
  }

  initPopular();

  /* ---------- Başlat ---------- */
  insertAdSlots();
  calcReadTime();
})();
