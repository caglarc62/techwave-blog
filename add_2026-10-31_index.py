# -*- coding: utf-8 -*-
"""31 Ekim makalesini search-index.json'a ekler (idempotent)."""
import io, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "search-index.json")
with io.open(p, encoding="utf-8") as f:
    data = json.load(f)

data = [x for x in data if x.get("s") != "2026-10-31-kasim-guvenlik-yamalari"]

entry = {
    "t": "Kasım 2026 Güvenlik Yamaları: Windows, macOS ve Linux'ta Kritik Güncellemeler",
    "s": "2026-10-31-kasim-guvenlik-yamalari",
    "c": "Siber Güvenlik",
    "e": "Kasım 2026 güvenlik yamalarında hangi sistemler hedefleniyor, öncelik nasıl belirlenmeli ve dağıtım otomasyonu nasıl kurulur?",
    "d": "31 Ekim 2026",
    "i": "https://techwaveblog.site/images/security-patch-nov-2026-1.svg",
    "h": (
        "Kasım 2026 Güvenlik Yamaları: Windows, macOS ve Linux'ta Kritik Güncellemeler | "
        "1. Microsoft Patch Salı: 94 güvenlik bildirimi | "
        "2. Apple Security Update: Ventura ve sonrası | "
        "3. Linux dağıtımları: Kernel 6.12.11 ve dağıtım yamaları | "
        "4. Kurumsal uygulama rehberi | "
        "5. Sıkça Sorulan Sorular | "
        "6. Sonuç"
    ),
    "x": (
        "Kasım 2026 güvenlik yamaları, yılın en kritik bakım dönemlerinden biri olarak öne çıkıyor. "
        "Microsoft, Apple ve büyük Linux dağıtımları aynı hafta içinde uzaktan kod çalıştırma, "
        "ayrıcalık yükseltme ve mikro mimari tabanlı sızıntılara karşı yamalar yayınladı."
    ),
}

data.insert(0, entry)
with io.open(p, "w", encoding="utf-8") as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=None))
print("search-index.json güncellendi")
