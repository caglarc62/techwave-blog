# -*- coding: utf-8 -*-
"""Yeni makaleyi index.html kart grid'ine ve sitemap.xml'e ekler (UTF-8)."""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
SLUG = "2026nin-en-iyi-10-oyunu-yilin-vazgecilmezleri"
HERO = "https://images.pexels.com/photos/19012057/pexels-photo-19012057.jpeg?auto=compress&cs=tinysrgb&w=1200"
TITLE = "2026'nın En İyi 10 Oyunu: Bu Yılın Vazgeçilmeyen Yapımları"
EXCERPT = ("2026'nın en iyi 10 oyunu: Starfall Horizon Protocol, Aetherbound, Ashen Covenant, Vector Strike "
           "Blacksite, Mochi and the Lighthouse, Nexus Rift, Apex Circuit 26, Iron Meridian, Silent Ward ve "
           "Bunker Nine; tür rehberi, ücretsiz/abonelik/tam satın alma bütçe tablosu, oyun bilisayarı "
           "gereksinimleri, konsol-PC-VR karşılaştırmaları ve SSS.")

CARD = (
    '        <!-- YENİ MAKALE — Otomatik eklendi -->\n'
    '        <article class="card" data-category="Oyun">\n'
    '          <div class="card-img"><img src="%s" alt="%s" loading="lazy"></div>\n'
    '          <div class="card-body">\n'
    '            <span class="card-tag" data-category="Oyun">Oyun</span>\n'
    '            <h2 class="card-title">\n'
    '              <a href="articles/%s.html">%s</a>\n'
    '            </h2>\n'
    '            <p class="card-excerpt">%s</p>\n'
    '            <div class="card-meta">\n'
    '              <span>📅 4 Ekim 2026</span>\n'
    '              <span>⏱️ 9 dk okuma</span>\n'
    '            </div>\n'
    '          </div>\n'
    '        </article>\n'
    '\n'
) % (HERO, TITLE, SLUG, TITLE, EXCERPT)

# --- index.html ---
idx_path = os.path.join(BASE, "index.html")
html = io.open(idx_path, encoding="utf-8").read()
if SLUG in html:
    print("index.html: makale zaten ekli, atlaniyor")
else:
    marker = '<!-- YENİ MAKALE'
    pos = html.find(marker)
    if pos == -1:
        raise SystemExit("YENİ MAKALE işareti bulunamadı")
    # kartın grid içinde olduğu yer: işaretin hemen öncesindeki <div class="card-grid">
    grid_pos = html.rfind('<div class="card-grid">', 0, pos)
    if grid_pos == -1:
        raise SystemExit("card-grid bulunamadı")
    insert_at = html.rfind("\n", 0, pos) + 1
    html = html[:insert_at] + CARD + html[insert_at:]
    io.open(idx_path, "w", encoding="utf-8").write(html)
    print("index.html: kart eklendi (pozisyon %d)" % insert_at)

# --- sitemap.xml ---
sm_path = os.path.join(BASE, "sitemap.xml")
sm = io.open(sm_path, encoding="utf-8").read()
loc = "https://techwaveblog.site/articles/%s.html" % SLUG
if loc in sm:
    print("sitemap.xml: URL zaten var, atlaniyor")
else:
    block = (
        "  <url>\n"
        "    <loc>%s</loc>\n"
        "    <lastmod>2026-10-04</lastmod>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>0.8</priority>\n"
        "  </url>\n"
        "</urlset>"
    ) % loc
    sm = sm.replace("</urlset>", block)
    io.open(sm_path, "w", encoding="utf-8").write(sm)
    print("sitemap.xml: URL eklendi")
