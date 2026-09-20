import sys
sys.path.insert(0, '.')
from update_index import rebuild_index
import os

articles_dir = os.path.join(os.path.dirname(__file__), "articles")
index_path = os.path.join(os.path.dirname(__file__), "index.html")

count = rebuild_index(index_path, articles_dir)
print(f"{count} makale ile index yeniden olusturuldu.")
