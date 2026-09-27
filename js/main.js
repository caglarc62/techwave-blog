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

  /* ---------- Başlat ---------- */
  insertAdSlots();
  calcReadTime();
})();
