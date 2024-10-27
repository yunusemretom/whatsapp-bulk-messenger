
# WhatsApp Bulk Messenger

WhatsApp Bulk Messenger, birden fazla telefon numarasına tek bir mesaj göndermenizi sağlayan bir otomasyon sistemidir. Kullanıcılar, mesaj metinlerini ve telefon numaralarını ayrı metin dosyalarında saklayabilirken, görseller, videolar ve diğer dosya türleri için yalnızca dosya yollarını içeren bir kod dosyası kullanılmaktadır.

## Özellikler

- **Otomatik Mesaj Gönderimi**: Belirtilen telefon numaralarına tek bir tıklama ile mesaj gönderebilir.
- **Medya Desteği**: JPG, PNG, PDF, ve MP4 gibi dosyaları mesajlarla birlikte gönderebilir.
- **Kullanıcı Dostu Arayüz**: Tarayıcı üzerinde WhatsApp Web ile etkileşim sağlayarak kullanıcı dostu bir deneyim sunar.

## Gereksinimler

- Python 3.x
- Selenium kütüphanesi
- Chrome WebDriver
- WhatsApp hesabı (Web üzerinden oturum açılmış olmalıdır)

## Kurulum

1. **Gereksinimleri yükleyin**:

   ```bash
   pip install selenium
   ```

2. **Chrome WebDriver'ı indirin**: [Chrome WebDriver](https://sites.google.com/chromium.org/driver/) sayfasından sisteminize uygun sürümü indirin ve `chromedriver.exe` dosyasını projenizin kök dizinine yerleştirin.

3. **Proje dosyalarını oluşturun**:
   - `message.txt`: Göndermek istediğiniz mesajı bu dosyaya yazın.
   - `numbers.txt`: Mesaj göndermek istediğiniz telefon numaralarını (ülke koduyla birlikte) her satıra bir numara gelecek şekilde yazın.

4. **Medya dosyalarını yerleştirin**: Göndermek istediğiniz resim, video ve diğer medya dosyalarını projenizin kök dizininde tutun.

## Kullanım

1. `bulk_messenger.py` dosyasını çalıştırın:

   ```bash
   python bulk_messenger.py
   ```

2. Tarayıcı açıldığında WhatsApp Web'e giriş yapın. (Bu işlemi bir kez yapmanız yeterlidir.)

3. Giriş tamamlandığında, komut isteminde talimatları izleyin ve ENTER tuşuna basın.

4. Mesaj gönderimi başlayacak ve gönderim durumu terminalde görüntülenecektir.

## Örnek Kod

Aşağıda temel kod yapısını görebilirsiniz:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import glob
from time import sleep
from urllib.parse import quote

# Tarayıcı ayarları
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
options.add_argument('--start-maximized')

# Mesaj ve numara dosyalarını oku
with open("message.txt", "r", encoding="utf8") as f:
    message = quote(f.read())

with open("numbers.txt", "r") as f:
    numbers = [line.strip() for line in f.readlines() if line.strip()]

# Mesaj gönderimi işlemleri
driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path="chromedriver.exe"), options=options)
driver.get('https://web.whatsapp.com')
input("Whatsapp Web'e giriş tamamlandıktan sonra ENTER tuşuna basın...")

for number in numbers:
    # Mesaj gönderim kodu buraya gelecek
    # ...
```

## Lisans

Bu proje, [MIT Lisansı](LICENSE) altında lisanslanmıştır.

## İletişim

Proje ile ilgili sorularınız için [email@example.com](mailto:email@example.com) adresi üzerinden iletişime geçebilirsiniz.

---

**Not**: Bu sistemin kullanımı, WhatsApp'ın kullanım şartlarına uygun olmalıdır. Spam gönderimi veya izinsiz mesaj gönderimi yasaktır.
```

Bu README dosyası, projenin özelliklerini, kurulum ve kullanım talimatlarını, örnek kodları içermekte ve okuyucuların kolayca anlayabilmesi için yapılandırılmıştır. İstediğin gibi düzenlemeler yapabilirsin.