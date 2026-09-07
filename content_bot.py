"""
content_bot.py — TechWave Otomatik İçerik Botu
Günde 1 makale otomatik üretir ve siteye ekler.

Kullanım:
    python content_bot.py              # Tek seferlik çalıştır
    python content_bot.py --schedule   # Günlük zamanlama ile çalıştır
    python content_bot.py --test       # Test modu (API ohne, rastgele makale)
"""

import os
import sys
import json
import time
import re
import logging
import argparse
from datetime import datetime

from dotenv import load_dotenv

# Modüller
import trends
import generate_article
import update_index
import images

# ==========================================================================
# AYARLAR
# ==========================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(SCRIPT_DIR, "config.json")
LOG_FILE = os.path.join(SCRIPT_DIR, "bot_log.json")
ARTICLES_DIR = os.path.join(SCRIPT_DIR, "articles")

load_dotenv(os.path.join(SCRIPT_DIR, ".env"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(SCRIPT_DIR, "bot.log"), encoding="utf-8"),
    ],
)
log = logging.getLogger("content_bot")


# ==========================================================================
# LOG
# ==========================================================================

def load_log():
    if not os.path.exists(LOG_FILE):
        return {"runs": [], "articles_generated": 0}
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"runs": [], "articles_generated": 0}


def save_log(data):
    try:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        log.error("Log kaydetme hatası: %s", e)


def log_run(success, article_title=None, error=None):
    data = load_log()
    data["runs"].append({
        "timestamp": datetime.now().isoformat(),
        "success": success,
        "article": article_title,
        "error": str(error) if error else None,
    })
    if success:
        data["articles_generated"] = data.get("articles_generated", 0) + 1
    # Son 100 çalıştırmayı tut
    data["runs"] = data["runs"][-100:]
    save_log(data)


# ==========================================================================
# ANA AKIŞ
# ==========================================================================

def run_once(config, test_mode=False):
    """Tek seferlik çalıştır — 1 makale üret ve yayımla."""
    log.info("=" * 60)
    log.info("İçerik botu başlatılıyor... (%s)", datetime.now().strftime("%Y-%m-%d %H:%M"))
    log.info("=" * 60)

    # 1. Konu seçimi
    log.info("1. Adım: Trendler taranıyor...")
    if test_mode:
        topic = trends.generate_random_topic()
        log.info("Test modu: Rastgele konu seçildi.")
    else:
        topic = trends.generate_topic_from_trends(config["trend_sources"])

    log.info("   Seçilen konu: %s — %s", topic["category"], topic["title"])

    # 2. Makale üretimi
    log.info("2. Adım: Claude API ile makale üretiliyor...")
    if test_mode:
        # Test modu: Sahte makale
        article = create_test_article(topic, config)
        log.info("   Test makalesi oluşturuldu.")
    else:
        article = generate_article.generate_article(topic, config)
        if article is None:
            log.error("Makale üretilemedi!")
            log_run(False, error="Makale üretilemedi")
            return False

    log.info("   Başlık: %s", article["title"])
    log.info("   Okuma süresi: %s", article["read_time"])

    # 3. HTML dosyası oluştur
    log.info("3. Adım: HTML dosyası oluşturuluyor...")
    html_path = render_article_html(article, config)
    if html_path is None:
        log.error("HTML dosyası oluşturulamadı!")
        log_run(False, article["title"], error="HTML oluşturma hatası")
        return False

    log.info("   Dosya: %s", html_path)

    # 4. Ana sayfayı güncelle
    log.info("4. Adım: Ana sayfa güncelleniyor...")
    site_dir = os.path.dirname(ARTICLES_DIR)
    success = update_index.update_index_html(article, site_dir)
    if success:
        log.info("   Ana sayfa güncellendi.")
    else:
        log.warning("   Ana sayfa güncellenemedi (makale yine de kaydedildi).")

    # 5. GitHub'a push et (Netlify otomatik deploy eder)
    deploy_to_github(config)

    # 6. Log kaydet
    log_run(True, article["title"])

    log.info("=" * 60)
    log.info("BAŞARILI! Makale yayımlandı: %s", article["title"])
    log.info("  Dosya: articles/%s.html", article["slug"])
    log.info("  Kategori: %s", article["category"])
    log.info("=" * 60)

    return True


def deploy_to_github(config):
    """Değişiklikleri GitHub'a push eder — Netlify otomatik deploy eder."""
    import subprocess

    github_url = config.get("github_url", "")
    if not github_url:
        log.warning("github_url config'de yok, deploy atlanıyor.")
        return False

    # Git yolunu bul
    git_cmd = "git"
    try:
        subprocess.run([git_cmd, "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Windows'ta varsayılan kurulum yolu
        git_paths = [
            r"C:\Program Files\Git\cmd\git.exe",
            r"C:\Program Files (x86)\Git\cmd\git.exe",
        ]
        for p in git_paths:
            if os.path.exists(p):
                git_cmd = p
                break
        else:
            log.warning("Git bulunamadı — deploy atlanıyor.")
            return False

    try:
        site_dir = os.path.dirname(ARTICLES_DIR)

        # Değişiklikleri ekle
        subprocess.run([git_cmd, "add", "-A"], cwd=site_dir, check=True, capture_output=True)

        # Değişiklik var mı kontrol et
        result = subprocess.run([git_cmd, "status", "--porcelain"], cwd=site_dir, capture_output=True, text=True)
        if not result.stdout.strip():
            log.info("Yeni değişiklik yok, push atlanıyor.")
            return True

        # Commit
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.run([git_cmd, "commit", "-m", f"Otomatik güncelleme: {now}"], cwd=site_dir, check=True, capture_output=True)

        # Push
        subprocess.run([git_cmd, "push"], cwd=site_dir, check=True, capture_output=True)
        log.info("GitHub'a push edildi — Netlify otomatik deploy başlatacak.")
        return True

    except subprocess.CalledProcessError as e:
        log.warning("GitHub push hatası: %s", e)
        return False


def create_test_article(topic, config):
    """Test modu için sahte makale üretir (API gerekmez)."""
    today = datetime.now()
    months_tr = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan",
        5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
        9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık",
    }
    date_str = f"{today.day} {months_tr[today.month]} {today.year}"

    result = {
        "title": topic["title"],
        "slug": re.sub(r'[^a-z0-9\s-]', '', topic["title"].lower()).replace(" ", "-").strip("-")[:50],
        "excerpt": f"{topic['category']} kategorisinde {topic['title']} hakkında bilgilendirici makale.",
        "content": f"""<h2>Giriş</h2>
<p>Bu makale <strong>{topic['title']}</strong> konusunu ele almaktadır. {topic['category']} alanında güncel gelişmeler ve önemli noktalar incelenmektedir.</p>

<h2>Neden Önemli?</h2>
<p>{topic['category']} alanında yaşanan gelişmeler, hem bireysel kullanıcıları hem de kurumları yakından ilgilendirmektedir. Bu konuyu anlamak, geleceğe hazırlanmak açısından kritik öneme sahiptir.</p>

<h2>Temel Noktalar</h2>
<ul>
<li>Güncel trendler ve gelişmeler</li>
<li>Pratik uygulama alanları</li>
<li>Geleceğe yönelik projeksiyonlar</li>
</ul>

<h3>1. Güncel Trendler</h3>
<p>{topic['category']} alanında 2026 yılına damgasını vuran gelişmeler bulunmaktadır. Bu gelişmeleri takip etmek, rekabet avantajı sağlar.</p>

<h3>2. Pratik Uygulamalar</h3>
<p>Teorik bilginin yanı sıra, bu bilgiyi pratikte nasıl kullanabileceğinizi de bilmeniz gerekir. Gerçek dünya senaryoları ve örnekler bu konuda yol gösterici olacaktır.</p>

<h3>3. Gelecek Projeksiyonları</h2>
<p>{topic['category']} alanının gelecekteki yönü hakkında öngörülerde bulunmak, stratejik kararlar almak için önemlidir.</p>

<blockquote>"{topic['category']} alanında kalmak için sürekli öğrenmek ve adapte olmak gereklidir."</blockquote>

<h2>Sonuç</h2>
<p>{topic['title']} konusunu anlamak ve takip etmek, günümüzün hızla değişen teknoloji dünyasında hayati önem taşımaktadır. Umarız bu makale sizin için faydalı olmuştur.</p>

<p><em>Bu makale TechWave tarafından hazırlanmıştır.</em></p>""",
        "meta_description": f"{topic['title']} — {topic['category']} hakkında kapsamlı bilgi ve rehber. 2026 güncellemeleri.",
        "tags": [topic["category"].lower(), "teknoloji", "2026", "rehber"],
        "category": topic["category"],
        "emoji": config.get("emoji_map", {}).get(topic["category"], "📝"),
        "gradient": config.get("gradient_map", {}).get(topic["category"], "linear-gradient(135deg, #667eea, #764ba2)"),
        "date": date_str,
        "date_iso": today.strftime("%Y-%m-%d"),
        "author": config.get("author", "TechWave"),
        "read_time": "5 dk okuma",
    }

    # Test modunda da fallback görsel çek
    try:
        image_info = images.get_article_image(topic["category"], topic["title"])
        result["image_url"] = image_info["url"]
        result["image_credit"] = image_info["credit"]
    except Exception as e:
        log.warning("Görsel çekme hatası: %s", e)
        result["image_url"] = ""
        result["image_credit"] = ""

    return result


def render_article_html(article, config):
    """Makale verisini HTML şablonuyla birleştirip dosyaya yazar."""
    template_path = os.path.join(SCRIPT_DIR, "templates", "article_template.html")

    if not os.path.exists(template_path):
        log.error("HTML şablonu bulunamadı: %s", template_path)
        return None

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Basit placeholder değiştirme
    replacements = {
        "{{ title }}": article.get("title", ""),
        "{{ slug }}": article.get("slug", ""),
        "{{ excerpt }}": article.get("excerpt", ""),
        "{{ content }}": article.get("content", ""),
        "{{ meta_description }}": article.get("meta_description", ""),
        "{{ category }}": article.get("category", ""),
        "{{ emoji }}": article.get("emoji", "📝"),
        "{{ gradient }}": article.get("gradient", ""),
        "{{ date }}": article.get("date", ""),
        "{{ date_iso }}": article.get("date_iso", ""),
        "{{ read_time }}": article.get("read_time", ""),
        "{{ author }}": article.get("author", "TechWave"),
        "{{ site_name }}": config.get("site_name", "TechWave"),
        "{{ site_url }}": config.get("site_url", "https://TechWave.com"),
        "{{ image_url }}": article.get("image_url", ""),
        "{{ image_credit }}": article.get("image_credit", ""),
    }

    # Etiketleri string olarak ekle
    tags = article.get("tags", [])
    tag_str = ", ".join(tags)
    replacements["{{ tags | join(', ') }}"] = tag_str

    html = template
    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    # Dosyaya yaz
    slug = article.get("slug", "yeni-makale")
    filename = f"{slug}.html"
    filepath = os.path.join(ARTICLES_DIR, filename)

    os.makedirs(ARTICLES_DIR, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    return filepath


# ==========================================================================
# ZAMANLAMA
# ==========================================================================

def run_scheduled(config):
    """Günlük zamanlama ile çalıştır (basit döngü)."""
    import schedule

    log.info("Günlük zamanlama modu başlatıldı.")
    log.info("Her gün saat 09:00'da çalışacak.")

    schedule.every().day.at("09:00").do(run_once, config=config)

    # İlk çalıştırmayı yap
    run_once(config)

    while True:
        schedule.run_pending()
        time.sleep(60)


# ==========================================================================
# ENTRY POINT
# ==========================================================================

def main():
    parser = argparse.ArgumentParser(description="TechWave İçerik Botu")
    parser.add_argument("--schedule", action="store_true", help="Günlük zamanlama ile çalıştır")
    parser.add_argument("--test", action="store_true", help="Test modu (API gerekmez)")
    args = parser.parse_args()

    # Config yükle
    if not os.path.exists(CONFIG_FILE):
        log.error("config.json bulunamadı: %s", CONFIG_FILE)
        sys.exit(1)

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)

    if args.schedule:
        run_scheduled(config)
    else:
        success = run_once(config, test_mode=args.test)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
