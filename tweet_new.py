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

HASHTAGS = {
    "Yapay Zeka": ["#yapayzeka", "#AI", "#teknoloji"],
    "AI Araçları": ["#AI", "#yapayzeka", "#araçlar"],
    "Yazılım": ["#yazılım", "#kodlama", "#teknoloji"],
    "Python": ["#python", "#kodlama", "#yazılım"],
    "Siber Güvenlik": ["#sibergüvenlik", "#güvenlik", "#teknoloji"],
    "Mobil": ["#mobil", "#teknoloji", "#akıllıtelefon"],
    "Donanım": ["#donanım", "#teknoloji", "#tech"],
    "Oyun": ["#oyun", "#gaming", "#teknoloji"],
    "Finans": ["#finans", "#ekonomi", "#teknoloji"],
    "Blockchain": ["#blockchain", "#kripto", "#teknoloji"],
}

GENERIC = ["#teknoloji", "#tech", "#2026"]


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

    return {"slug": slug, "title": title, "category": category, "hero": hero}


def build_tweet(article):
    url = SITE + "/articles/" + article["slug"] + ".html"
    tags = HASHTAGS.get(article["category"], GENERIC)
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
