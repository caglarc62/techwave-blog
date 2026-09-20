import os
import re
import glob

articles_dir = os.path.join(os.path.dirname(__file__), "articles")
index_path = os.path.join(os.path.dirname(__file__), "index.html")

MANUAL = {
    "yapay-zeka-ile-nasil-para-kazanilir": {
        "title": "2026'da Yapay Zeka ile Nasıl Para Kazanılır? 8 Kanıtlanmış Yol",
        "category": "Yapay Zeka",
        "date": "20 Eylül 2026",
        "read_time": "7 dk okuma",
        "excerpt": "Yapay zeka araçlarını kullanarak gelir elde etmenin 8 yolu ve pratik ipuçları.",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200",
    },
    "siber-guvenlik-101-kisisel-verilerinizi-nasil-korursunuz": {
        "title": "Siber Güvenlik 101: Kişisel Verilerinizi Nasıl Korursunuz?",
        "category": "Siber Güvenlik",
        "date": "20 Eylül 2026",
        "read_time": "7 dk okuma",
        "excerpt": "2026 yılında kişisel verilerinizi koruma rehberi.",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200",
    },
    "chatgpt-vs-clude-vs-gemini-karsilastirma": {
        "title": "ChatGPT vs Claude vs Gemini: 2026'da Hangi AI Aracı Daha İyi?",
        "category": "AI Araçları",
        "date": "20 Eylül 2026",
        "read_time": "8 dk okuma",
        "excerpt": "ChatGPT, Claude ve Gemini karşılaştırması 2026.",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200",
    },
    "2026-telefon-alirken-5-kritik-hata": {
        "title": "2026'da Akıllı Telefon Alırken Yapılan 5 Kritik Hata",
        "category": "Mobil",
        "date": "19 Eylül 2026",
        "read_time": "6 dk okuma",
        "excerpt": "Doğru telefon seçimi için bilmeniz gereken 5 hata.",
        "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=1200",
    },
    "2026-piyasa-dinamikleri-algoritmik-ticaret-kripto": {
        "title": "2026 Piyasa Dinamikleri: Algoritmik Ticaret ve Kripto",
        "category": "Finans",
        "date": "20 Eylül 2026",
        "read_time": "6 dk okuma",
        "excerpt": "Küresel faiz politikaları, BIST 100, Bitcoin ETF.",
        "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1200",
    },
    "2026-isletim-sistemi-ve-kodlama-teknoloji-trendleri": {
        "title": "2026 İşletim Sistemi ve Kodlama Teknoloji Trendleri",
        "category": "Yazılım",
        "date": "20 Eylül 2026",
        "read_time": "5 dk okuma",
        "excerpt": "Yerleşik yapay zeka, on-device AI, cross-platform diller.",
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200",
    },
    "google-gemini-yapay-zeka-guvenlik-testi-sirketlere-sizdi": {
        "title": "Google Gemini Güvenlik Testinde Şirket Sınırlarını Aştı",
        "category": "Siber Güvenlik",
        "date": "19 Eylül 2026",
        "read_time": "5 dk okuma",
        "excerpt": "Google Gemini güvenlik testinde şirketlerin savunma hatlarını aştı.",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200",
    },
    "abd-universitelerinde-en-cok-ogretilen-dil-python": {
        "title": "ABD Üniversitelerinin Favori Programlama Dili: Python",
        "category": "Python",
        "date": "18 Eylül 2026",
        "read_time": "6 dk okuma",
        "excerpt": "ABD üniversitelerinde Python neden zirvede?",
        "image_url": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1200",
    },
    "python-nedir-bilmeniz-gereken-her-sey": {
        "title": "Python Nedir? Sıfırdan İleri Seviyeye Bilmeniz Gereken Her Şey",
        "category": "Python",
        "date": "16 Eylül 2026",
        "read_time": "6 dk okuma",
        "excerpt": "Python nedir, ne işe yarar ve nasıl öğrenilir?",
        "image_url": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1200",
    },
    "insaat-endustrisi-icin-en-iyi-10-ai-araci-eylul-2026": {
        "title": "İnşaat Endüstrisi için En İyi 10 AI Aracı Eylül 2026",
        "category": "Yapay Zeka",
        "date": "16 Eylül 2026",
        "read_time": "5 dk okuma",
        "excerpt": "İnşaat sektörünü dönüştüren en iyi 10 yapay zeka aracı.",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200",
    },
    "blockchain-yazilimi-en-iyi-11-programlama-dili": {
        "title": "Blockchain Yazılımında En İyi 11 Programlama Dili",
        "category": "Blockchain",
        "date": "16 Eylül 2026",
        "read_time": "6 dk okuma",
        "excerpt": "Web3 için en iyi 11 programlama dili rehberi.",
        "image_url": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1200",
    },
    "ab-15-yas-alti-oyun-kisitlamasi-dijital-duzenleme": {
        "title": "AB 15 Yaş Altı Çocuklara Oyun Kısıtlaması Getiriyor",
        "category": "Oyun",
        "date": "16 Eylül 2026",
        "read_time": "5 dk okuma",
        "excerpt": "AB'nin 15 yaş altı oyun kısıtlaması kararı ve detayları.",
        "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1200",
    },
    "apple-yapay-zeka-destekli-saglik-uygulamasi": {
        "title": "Apple Yapay Zeka Destekli Yeni Sağlık Uygulamasını Duyurdu",
        "category": "Mobil",
        "date": "12 Eylül 2026",
        "read_time": "4 dk okuma",
        "excerpt": "Apple'ın yapay zeka destekli yeni sağlık uygulaması.",
        "image_url": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200",
    },
}

# Makaleleri tara
articles = []
seen = set()
for filepath in sorted(glob.glob(os.path.join(articles_dir, "*.html")), reverse=True):
    slug = os.path.splitext(os.path.basename(filepath))[0]
    if slug in seen:
        continue
    seen.add(slug)

    if slug in MANUAL:
        m = MANUAL[slug]
        articles.append({
            "title": m["title"],
            "slug": slug,
            "excerpt": m["excerpt"],
            "category": m["category"],
            "image_url": m["image_url"],
            "date": m["date"],
            "read_time": m["read_time"],
        })
    else:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        m = re.search(r'<title>(.*?)—', content)
        title = m.group(1).strip() if m else "Yeni Makale"

        m = re.search(r'<meta name="description" content="(.*?)"', content)
        excerpt = m.group(1) if m else ""

        m = re.search(r'<span class="card-tag"[^>]*>(.*?)</span>', content)
        category = m.group(1) if m else "Teknoloji"

        m = re.search(r'<meta property="og:image" content="(.*?)"', content)
        image_url = m.group(1) if m else ""

        m = re.search(r'📅\s*(.*?)<', content)
        date = m.group(1).strip() if m else ""

        m = re.search(r'⏱️\s*(.*?)<', content)
        read_time = m.group(1).strip() if m else "5 dk okuma"

        articles.append({
            "title": title,
            "slug": slug,
            "excerpt": excerpt,
            "category": category,
            "image_url": image_url,
            "date": date,
            "read_time": read_time,
        })

# Tarihe göre sırala
def parse_date(d):
    months = {"Ocak":1,"Şubat":2,"Mart":3,"Nisan":4,"Mayıs":5,"Haziran":6,
              "Temmuz":7,"Ağustos":8,"Eylül":9,"Ekim":10,"Kasım":11,"Aralık":12}
    parts = d.split()
    if len(parts) >= 3:
        try:
            return (int(parts[2]), months.get(parts[1], 0), int(parts[0]))
        except:
            pass
    return (0, 0, 0)

articles.sort(key=lambda x: parse_date(x.get("date", "")), reverse=True)

# Oluştur
def make_card(art):
    cat = art["category"]
    img = f'<img src="{art["image_url"]}" alt="{art["title"]}" loading="lazy">' if art["image_url"] else f'<div style="display:flex;align-items:center;justify-content:center;color:#fff;font-size:2rem;height:100%;background:linear-gradient(135deg,#6366f1,#a855f7);">📝</div>'
    return f'''        <article class="card" data-category="{cat}">
          <div class="card-img">{img}</div>
          <div class="card-body">
            <span class="card-tag" data-category="{cat}">{cat}</span>
            <h2 class="card-title">
              <a href="articles/{art["slug"]}.html">{art["title"]}</a>
            </h2>
            <p class="card-excerpt">{art["excerpt"]}</p>
            <div class="card-meta">
              <span>📅 {art["date"]}</span>
              <span>⏱️ {art["read_time"]}</span>
            </div>
          </div>
        </article>'''

# İlk makaleyi öne çıkan yap
featured = articles[0] if articles else None
rest = articles[1:] if len(articles) > 1 else []

featured_html = ""
if featured:
    img = f'<img src="{featured["image_url"]}" alt="{featured["title"]}" loading="eager">' if featured["image_url"] else ""
    featured_html = f'''      <div class="featured-post">
        <article class="featured-card">
          <div class="card-img">
            {img}
          </div>
          <div class="card-body">
            <span class="featured-badge">⭐ Öne Çıkan</span>
            <span class="card-tag" data-category="{featured["category"]}">{featured["category"]}</span>
            <h2 class="card-title">
              <a href="articles/{featured["slug"]}.html">{featured["title"]}</a>
            </h2>
            <p class="card-excerpt">{featured["excerpt"]}</p>
            <div class="card-meta">
              <span>📅 {featured["date"]}</span>
              <span>⏱️ {featured["read_time"]}</span>
            </div>
          </div>
        </article>
      </div>'''

cards_html = "\n\n".join(make_card(a) for a in rest)

# Footer'daki popüler yazıları güncelle
popular_3 = articles[:3]
popular_html = "\n".join(f'          <li><a href="articles/{a["slug"]}.html">{a["title"]}</a></li>' for a in popular_3)

html = f'''<!DOCTYPE html>
<html lang="tr" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Teknoloji, yapay zeka ve yazılım dünyasından en güncel yazılar. AI rehberleri, Python eğitimleri ve teknoloji haberleri.">
  <meta name="keywords" content="yapay zeka, teknoloji, yazılım, python, chatgpt, AI, programlama">
  <meta name="author" content="TechWave">
  <meta name="robots" content="index, follow">
  <title>TechWave — Teknoloji, AI ve Yazılım Blogu</title>

  <meta property="og:title" content="TechWave — Teknoloji, AI ve Yazılım Blogu">
  <meta property="og:description" content="Yapay zeka, yazılım ve teknoloji dünyasından güncel yazılar.">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="tr_TR">

  <link rel="canonical" href="https://techwaveblog.site/">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/style.css">

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Blog",
    "name": "TechWave",
    "description": "Teknoloji, yapay zeka ve yazılım blogu",
    "url": "https://techwaveblog.site",
    "inLanguage": "tr"
  }}
  </script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3459052960619900" crossorigin="anonymous"></script>
</head>
<body>

  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="logo"><img src="images/logo.svg" alt="TechWave"></a>
      <button class="mobile-menu-btn" aria-label="Menü">☰</button>
      <nav>
        <a href="index.html" class="active">Ana Sayfa</a>
        <a href="kategori.html">Kategoriler</a>
        <a href="iletisim.html">İletişim</a>
        <button class="theme-toggle" aria-label="Tema Değiştir">🌙</button>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="container">
      <div class="badge">🚀 Teknoloji ve Yapay Zeka Blogu</div>
      <h1>Teknoloji, Yapay Zeka ve<br>Yazılım Dünyası</h1>
      <p>Yazılım, yapay zeka ve teknoloji dünyasından güncel yazılar, rehberler ve analizler. Geleceği birlikte keşfedelim.</p>
    </div>
  </section>

  <div class="container">
    <div class="ad-slot ad-slot-728">
      <span>Reklam Alanı — 728×90</span>
    </div>
  </div>

  <div class="container content-layout">
    <main>
{featured_html}

      <div class="card-grid">

{cards_html}

      </div>
    </main>

    <aside class="sidebar">
      <div class="sidebar-widget">
        <h3>Popüler Yazılar</h3>
        <ul class="popular-list">
{popular_html}
        </ul>
      </div>

      <div class="ad-slot ad-slot-300x600">
        <span>Reklam Alanı — 300×600</span>
      </div>

      <div class="sidebar-widget">
        <h3>Kategoriler</h3>
        <div class="tag-cloud">
          <a href="kategori.html" class="tag">Yapay Zeka</a>
          <a href="kategori.html" class="tag">Yazılım</a>
          <a href="kategori.html" class="tag">Python</a>
          <a href="kategori.html" class="tag">AI Araçları</a>
          <a href="kategori.html" class="tag">Siber Güvenlik</a>
          <a href="kategori.html" class="tag">Mobil</a>
          <a href="kategori.html" class="tag">Oyun</a>
        </div>
      </div>
    </aside>
  </div>

  <div class="container">
    <div class="newsletter-cta">
      <h3>📬 TechWave Bültenine Katılın</h3>
      <p>Her hafta yapay zeka, yazılım ve teknoloji dünyasından en güncel gelişmeler doğrudan e-posta kutuna gelsin.</p>
      <form class="newsletter-form" onsubmit="event.preventDefault(); alert('Teşekkürler! Bültenimize başarıyla katıldınız.');">
        <input type="email" placeholder="E-posta adresiniz" required>
        <button type="submit">Katıl</button>
      </form>
    </div>
  </div>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="logo"><img src="images/logo.svg" alt="TechWave"></a>
          <p>Teknoloji, yapay zeka ve yazılım dünyasından güncel yazılar ve rehberler. 2026'dan beri aktif.</p>
        </div>
        <div>
          <h3 style="font-size:.95rem; margin-bottom:12px;">Sayfalar</h3>
          <ul class="footer-links">
            <li><a href="index.html">Ana Sayfa</a></li>
            <li><a href="kategori.html">Kategoriler</a></li>
            <li><a href="hakkimizda.html">Hakkımızda</a></li>
            <li><a href="gizlilik-politikasi.html">Gizlilik Politikası</a></li>
            <li><a href="iletisim.html">İletişim</a></li>
          </ul>
        </div>
        <div>
          <h3 style="font-size:.95rem; margin-bottom:12px;">Kategoriler</h3>
          <ul class="footer-links">
            <li><a href="kategori.html">Yapay Zeka</a></li>
            <li><a href="kategori.html">Yazılım</a></li>
            <li><a href="kategori.html">Python</a></li>
            <li><a href="kategori.html">AI Araçları</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 TechWave. Tüm hakları saklıdır.</p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>'''

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Index temizlendi! {len(articles)} benzersiz makale eklendi.")
