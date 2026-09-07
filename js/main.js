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

  /* ---------- Reklam Slotları (AdSense Yerleşimi) ---------- */
  function insertAdSlots() {
    var content = document.querySelector('.article-content');
    if (!content) return;

    var paragraphs = content.querySelectorAll('p');
    if (paragraphs.length < 4) return;

    // 3. paragraf sonrası orta reklam
    var midAd = document.createElement('div');
    midAd.className = 'ad-slot ad-slot-336';
    midAd.setAttribute('data-ad-slot', 'ORTA_REKLAM_ID');
    midAd.innerHTML = '<span>Reklam Alanı — 336×280</span>';
    paragraphs[3].parentNode.insertBefore(midAd, paragraphs[3].nextSibling);

    // İçerik sonu reklam
    var endAd = document.createElement('div');
    endAd.className = 'ad-slot ad-slot-728';
    endAd.setAttribute('data-ad-slot', 'SON_REKLAM_ID');
    endAd.innerHTML = '<span>Reklam Alanı — 728×90</span>';
    content.appendChild(endAd);
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
  var contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = contactForm.querySelector('.btn');
      btn.textContent = 'Gönderildi!';
      btn.style.background = '#10b981';
      setTimeout(function () {
        btn.textContent = 'Gönder';
        btn.style.background = '';
        contactForm.reset();
      }, 2500);
    });
  }

  /* ---------- Başlat ---------- */
  insertAdSlots();
  calcReadTime();
})();
