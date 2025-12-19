# 🛰️ Deep Learning Dataset Scraper (Selenium & Python)

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Chrome](https://img.shields.io/badge/Chrome-Driver-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white)
![Status](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

Bu araç, özellikle **Teknofest (Robotaksi, Model Uydu)** ve **Computer Vision** projelerinizde özgün görsel veri seti oluşturmak için geliştirilmiş, hızlı ve güvenilir bir scraping (kazıyıcı) çözüm sunar.

---

## 🛠️ Teknik Mimari ve Akış

Klasik scraper'lardan farklı olarak, Google Görseller'in dinamik yapısını ve pagination (sayfa) mekanizmasını DOM manipülasyonlarıyla aşar. Böylece "lazy-loading", sonsuz kaydırma ve tekrar eden görseller gibi sıkıntıları otomatik olarak çözer.

### 🚀 Temel Özellikler

- **Akıllı Sayfalama (Smart Pagination):** `start={index}` üzerinden ileri atlama ile hızlı ve stabilize kazıma.
- **Çift Kayıt Önleme:** `set()` yapısı ile görsel linklerinde tekrar engellenir.
- **Kalite Filtreleme:** 50x50px altında kalan küçük ikon ve thumb görseller otomatik olarak elenir.
- **İnsan Müdahalesi (Human-in-the-Loop):** CAPTCHA veya bot engeli çıktığında, terminal uyarısı ile manuel müdahale mümkün.

---

## 📦 Kurulum ve Kullanım

### 1. Gereksinimler

- Sisteminizde **Google Chrome** kurulu olmalıdır.
- Python 3.8+ gereklidir.

```bash
pip install selenium requests
```

### 2. Yapılandırma

`main.py` dosyasındaki aşağıdaki değişkenleri kendinize göre düzenleyin:

| Değişken           | Açıklama                                 |
|--------------------|------------------------------------------|
| `hedef_sayi`       | İndirilecek toplam görsel adedi          |
| `arama_kelimesi`   | Aranacak anahtar kelime (ör: "araba")    |
| `kayit_klasoru`    | Görsellerin kaydedileceği klasör         |

### 3. Çalıştırma

1. Script'i başlatın:
   ```bash
   python main.py
   ```
2. Eğer tarayıcıda CAPTCHA veya bot engeli çıkarsa, manuel olarak çözün ve terminalde "devam" komutunu verin.

---

## 🔬 Teknik Detaylar

- **DOM Interaction:** Görsellerin yüklenmesi için JavaScript `window.scrollTo` ile dinamik kaydırma yapılır.
- **User-Agent Spoofing:** Güncel tarayıcı başlıkları ile bot algılamaya karşı mukavemet.
- **Robust Error Handling:** Hatalı bağlantılarda ve geçersiz görsellerde `try-except` blokları ile dayanıklı çalışma.

---

## 📜 Lisans

Bu proje [MIT Lisansı](LICENSE) altındadır. Tamamen **araştırma ve eğitim amacıyla** geliştirilmiştir.

---

Her türlü katkı, öneri ve hata bildirimi için [issue açabilirsiniz](https://github.com/UmitOzteker/image-scraping-automation/issues).
