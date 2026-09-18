"""
run_multiple.py — Birden fazla makale üretir (bekleme süreli)
Kullanım: python run_multiple.py 5 (5 makale üret)
"""
import sys
import time
import subprocess

def run_bot():
    result = subprocess.run(
        ["python", "content_bot.py"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return result.returncode == 0

def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    
    print(f"Toplam {count} makale uretilecek.")
    print("=" * 50)
    
    for i in range(1, count + 1):
        print(f"\n--- Makale {i}/{count} ---")
        success = run_bot()
        
        if success:
            print(f"Makale {i} basarili!")
        else:
            print(f"Makale {i} basarisiz!")
        
        if i < count:
            wait = 70
            print(f"{wait} saniye bekleniyor...")
            time.sleep(wait)
    
    print("\n" + "=" * 50)
    print("Tamamlandi!")

if __name__ == "__main__":
    main()
