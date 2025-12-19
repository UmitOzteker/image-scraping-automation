import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ==========================================
# 1. AYARLAR
# ==========================================
hedef_sayi = 400
arama_kelimesi = "american futball ball"
kayit_klasoru = r"kayit_klasoru"
indirilen_linkler = set()  # Aynı resmi tekrar indirmemek için hafıza

if not os.path.exists(kayit_klasoru):
    os.makedirs(kayit_klasoru)

# ==========================================
# 2. TARAYICIYI AÇ
# ==========================================
chrome_options = Options()
chrome_options.add_argument("--lang=tr")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

# ==========================================
# 3. URL HESAPLAMA VE İNDİRME DÖNGÜSÜ
# ==========================================
toplam_indirilen = 0
sayfa_indeksi = 0  # 0, 20, 40, 60 diye artacak

print("\n--- PROGRAM BAŞLIYOR ---")
print("Robot kontrolü çıkarsa LÜTFEN ÇÖZ. Kod URL değiştirerek devam edecek.")

# Google'a ilk giriş (Sadece bot kontrolünü aşman için)
driver.get("https://www.google.com/imghp?hl=tr")
input("Robot kontrolünü çözdüysen ve hazırsan ENTER'a bas...")

while toplam_indirilen < hedef_sayi:

    # URL OLUŞTURMA (Butona tıklamak yok, direkt adrese gidiyoruz)
    # start= parametresi sayfayı belirler.
    yeni_url = f"https://www.google.com/search?q={arama_kelimesi}&tbm=isch&hl=tr&start={sayfa_indeksi}"

    print(f"\n>> Yeni Sayfaya Gidiliyor (Start: {sayfa_indeksi})")
    driver.get(yeni_url)

    # Sayfa yüklensin diye bekle
    time.sleep(4)

    # Aşağı kaydır ki resimler yüklensin (Javascript ile)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # Resimleri Bul
    resimler = driver.find_elements(By.TAG_NAME, "img")
    print(f"Bu sayfada {len(resimler)} resim bulundu. Taranıyor...")

    sayfa_resim_sayaci = 0  # Bu sayfadan kaç tane indirdik?

    for resim in resimler:
        if toplam_indirilen >= hedef_sayi:
            break

        try:
            # Resim linkini al
            src_linki = resim.get_attribute("src")
            if not src_linki:
                src_linki = resim.get_attribute("data-src")

            # Link geçerli mi ve daha önce indirdik mi?
            if src_linki and src_linki.startswith("http") and src_linki not in indirilen_linkler:

                genislik = resim.size.get('width')
                yukseklik = resim.size.get('height')

                # 50x50'den büyükse indir
                if genislik > 50 and yukseklik > 50:
                    veri = requests.get(src_linki, timeout=5).content
                    dosya_yolu = os.path.join(kayit_klasoru, f"top_{toplam_indirilen + 1}.jpg")

                    with open(dosya_yolu, "wb") as f:
                        f.write(veri)

                    indirilen_linkler.add(src_linki)
                    toplam_indirilen += 1
                    sayfa_resim_sayaci += 1
                    print(f"[{toplam_indirilen}/{hedef_sayi}] İndirildi")

        except Exception:
            continue

    # Eğer bu sayfadan hiç resim çıkmadıysa veya çok az çıktıysa Google bizi engellemiş olabilir
    # Yine de sonraki sayfayı deneyelim.
    if sayfa_resim_sayaci == 0:
        print("!!! Bu sayfadan resim indirilemedi. Diğer sayfaya geçiliyor...")

    # Sonraki sayfa için indeksi artır (Google genelde sayfa başına 20-50 sonuç gösterir)
    # Biz garantilemek için 20 artırıyoruz.
    sayfa_indeksi += 20

    # Çok hızlı gidip banlanmamak için kısa bir mola
    time.sleep(2)

print(f"\nİşlem tamamlandı. Toplam {toplam_indirilen} resim indirildi.")
driver.quit()