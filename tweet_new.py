# -*- coding: utf-8 -*-
"""
tweet_new.py — Yeni makaleler için hazır tweet metni üretir.

Kullanım:
    python tweet_new.py            # Paylaşılmamış makalelerin tweet metinlerini gösterir
    python tweet_new.py --mark     # En yeni paylaşılmamış makaleyi "paylaşıldı" olarak işaretler
    python tweet_new.py --mark <slug>   # Belirli slug'ı işaretler
    python tweet_new.py --all      # Tüm makalelerin tweet metinlerini gösterir (işaret bakmaksızın)
    python tweet_new.py --reset    # İşaretleri sıfırla

Tweet metnini kopyalayıp X'e yapıştır; görsel için makalenin hero görselini de ekle.
"""

import glob
import html
import io
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
MARK_FILE = os.path.join(BASE, "tweeted.json")
SITE = "https://techwaveblog.site"

# Başlık/özet içindeki kelimelere göre eşleşen hashtag'ler.
# Sıra önemlidir: en spesifik olan önce.
KEYWORD_TAGS = [
    ("chatgpt", "#ChatGPT"),
    ("claude", "#ClaudeAI"),
    ("gemini", "#GeminiAI"),
    ("copilot", "#GitHubCopilot"),
    ("cursor", "#Cursor"),
    ("midjourney", "#Midjourney"),
    ("stable diffusion", "#StableDiffusion"),
    ("dall", "#DALL-E"),
    ("sora", "#SoraAI"),
    ("deepseek", "#DeepSeek"),
    ("yapay zeka", "#YapayZeka"),
    ("yapay zekâ", "#YapayZeka"),
    ("ai ajan", "#AIAjanlari"),
    ("ajan", "#AIAjanlari"),
    ("yapay zeka", "#AI"),
    ("python", "#Python"),
    ("javascript", "#JavaScript"),
    ("kodlama", "#Kodlama"),
    ("yazılım", "#Yazılım"),
    ("geliştirme", "#Yazılım"),
    ("iphone", "#iPhone"),
    ("apple", "#Apple"),
    ("samsung", "#Samsung"),
    ("galaxy", "#Galaxy"),
    ("android", "#Android"),
    ("whatsapp", "#WhatsApp"),
    ("meta", "#Meta"),
    ("quest", "#VR"),
    ("vision pro", "#AppleVisionPro"),
    ("vr", "#VR"),
    ("notebook", "#Notebook"),
    ("laptop", "#Laptop"),
    ("tablet", "#Tablet"),
    ("ipad", "#iPad"),
    ("akıllı saat", "#SmartWatch"),
    ("kulaklık", "#Kulaklık"),
    ("robot süpürge", "#RobotSupurge"),
    ("oyun konsolu", "#OyunKonsolu"),
    ("playstation", "#PlayStation"),
    ("xbox", "#Xbox"),
    ("nintendo", "#Nintendo"),
    ("oyun", "#Oyun"),
    ("vpn", "#VPN"),
    ("siber", "#SiberGüvenlik"),
    ("güvenlik", "#Güvenlik"),
    ("antivirüs", "#Antivirus"),
    ("kripto", "#Kripto"),
    ("blockchain", "#Blockchain"),
    ("bitcoin", "#Bitcoin"),
    ("finans", "#Finans"),
    ("para kazan", "#ParaKazanma"),
    ("kazanma", "#Gelir"),
    ("seo", "#SEO"),
    ("google", "#Google"),
    ("wordpress", "#WordPress"),
    ("html", "#HTML"),
    ("web sitesi", "#WebGeliştirme"),
    ("mobil", "#MobilGeliştirme"),
    ("flutter", "#Flutter"),
    ("react", "#React"),
    ("trend", "#TeknolojiTrendleri"),
    ("teknoloji", "#Teknoloji"),
    ("internet", "#İnternet"),
    ("robot", "#Robotik"),
    ("sağlık", "#Sağlık"),
    ("spor", "#Spor"),
    ("blockchain", "#Web3"),
    ("enerji", "#YeşilTeknoloji"),
    ("kuantum", "#KuantumBilgisayar"),
    ("uzay", "#UzayTeknolojisi"),
]

# Kitleyi genişleten popüler genel hashtag havuzu (gündemle ilgili, çok aranan)
TRENDING_POOL = [
    "#AI", "#Teknoloji", "#2026", "#tech", "#YapayZeka",
    "#Yazılım", "#DijitalDünya", "#İnovasyon", "#Startup",
    "#GelecekTeknolojileri", "#DijitalDönüşüm",
]

GENERIC = ["#Teknoloji", "#2026", "#AI"]


def pick_hashtags(text, category):
    """Başlık+özet metninden konuya uygun hashtag seçer."""
    low = text.lower()
    matched = []
    seen = set()
    for kw, tag in KEYWORD_TAGS:
        if kw in low and tag.lower() not in seen:
            matched.append(tag)
            seen.add(tag.lower())
        if len(matched) >= 4:
            break

    # Havuzdan kitle genişleten 1-2 popüler tag ekle
    import random
    extra = [t for t in TRENDING_POOL if t.lower() not in seen]
    random.seed(sum(ord(ch) for ch in text))  # aynı makalede tutarlı seçim
    picked = matched[:3]
    for t in random.sample(extra, min(2, len(extra))):
        picked.append(t)

    if not picked:
        picked = HASHTAGS_BY_CATEGORY.get(category, GENERIC)
    return picked[:5]


HASHTAGS_BY_CATEGORY = {
    "Yapay Zeka": ["#YapayZeka", "#AI", "#Teknoloji"],
    "AI Araçları": ["#AI", "#YapayZeka", "#Araçlar"],
    "Yazılım": ["#Yazılım", "#Kodlama", "#Teknoloji"],
    "Python": ["#Python", "#Kodlama", "#Yazılım"],
    "Siber Güvenlik": ["#SiberGüvenlik", "#Güvenlik", "#Teknoloji"],
    "Mobil": ["#Mobil", "#Teknoloji", "#AkıllıTelefon"],
    "Donanım": ["#Donanım", "#Teknoloji", "#Tech"],
    "Oyun": ["#Oyun", "#Gaming", "#Teknoloji"],
    "Finans": ["#Finans", "#Ekonomi", "#Teknoloji"],
    "Blockchain": ["#Blockchain", "#Kripto", "#Teknoloji"],
}


def load_marks():
    if os.path.exists(MARK_FILE):
        with io.open(MARK_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"posted": []}


def save_marks(marks):
    with io.open(MARK_FILE, "w", encoding="utf-8") as f:
        json.dump(marks, f, ensure_ascii=False, indent=2)


def parse_article(path):
    with io.open(path, encoding="utf-8") as f:
        c = f.read()

    slug = os.path.splitext(os.path.basename(path))[0]

    m = re.search(r"<title>(.*?)</title>", c, re.DOTALL)
    title = m.group(1).strip() if m else slug
    title = html.unescape(title)
    title = re.sub(r"\s*[—–-]\s*(TechWave|TechWave — Teknoloji, AI ve Yazılım Blogu)\s*$", "", title)

    m = re.search(r'data-category="([^"]+)"', c)
    category = m.group(1) if m else ""

    m = re.search(r'(?:og:image"\s+content=|<meta property="og:image" content=)"([^"]+)"', c)
    hero = m.group(1) if m else ""
    if not hero:
        m = re.search(r'<img src="([^"]+)"', c)
        hero = m.group(1) if m else ""

    m = re.search(r'<meta name="description" content="([^"]+)"', c)
    desc = html.unescape(m.group(1)) if m else ""

    return {"slug": slug, "title": title, "category": category, "hero": hero, "desc": desc}


def build_tweet(article):
    url = SITE + "/articles/" + article["slug"] + ".html"
    tags = pick_hashtags(article["title"] + " " + article.get("desc", ""), article["category"])
    tags_str = " ".join(tags)

    # X: link 23 karakter sayılır, toplam limit 280
    link_len = 23
    hashtags_len = len(tags_str) + 2  # \n\n
    base = "\n\n" + url + "\n\n" + tags_str
    budget = 280 - link_len - hashtags_len - 5  # başlık payı

    title = article["title"]
    if len(title) > budget:
        title = title[: budget - 1].rstrip() + "…"

    return "🆕 Yeni makale!\n\n" + title + base


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = sys.argv[1:]
    marks = load_marks()
    posted = set(marks.get("posted", []))

    if "--reset" in args:
        save_marks({"posted": []})
        print("İşaretler sıfırlandı.")
        return

    articles = [parse_article(p) for p in sorted(glob.glob(os.path.join(BASE, "articles", "*.html")))]
    articles.sort(key=lambda a: a["slug"])

    if "--mark-all" in args:
        save_marks({"posted": [a["slug"] for a in articles]})
        print("Tüm makaleler işaretlendi:", len(articles))
        return

    show_all = "--all" in args

    if "--mark" in args:
        i = args.index("--mark")
        if len(args) > i + 1 and not args[i + 1].startswith("--"):
            slug = args[i + 1]
        else:
            pending = [a for a in articles if a["slug"] not in posted]
            if not pending:
                print("İşaretlenmemiş makale yok.")
                return
            slug = pending[-1]["slug"]
        if slug in posted:
            print("Zaten işaretli:", slug)
            return
        posted.add(slug)
        save_marks({"posted": sorted(posted)})
        print("İşaretlendi:", slug)
        return

    pending = articles if show_all else [a for a in articles if a["slug"] not in posted]

    if not pending:
        print("Paylaşılacak yeni makale yok. (--all ile hepsini görebilirsin)")
        return

    print("=" * 60)
    for a in pending:
        print(build_tweet(a))
        print()
        print("Hero görsel:", a["hero"] or "(yok)")
        print("-" * 60)

    print("Kopyala → X'e yapıştır → bitirince: python tweet_new.py --mark <slug>")


if __name__ == "__main__":
    main()
