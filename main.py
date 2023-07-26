# requests ve BeautifulSoup kütüphanelerini içe aktarın
import requests
from bs4 import BeautifulSoup

# pandas kütüphanesini içe aktarın
import pandas as pd

# URL'yi tanımlayın
url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=%C4%B0stanbul&ilce=Ata%C5%9Fehir"

# URL'ye bir GET isteği gönderin ve yanıtı alın
response = requests.get(url)

# Yanıtın durum kodunu kontrol edin
if response.status_code == 200:
    print("Başarılı istek")
else:
    print("Başarısız istek")

# Yanıtın içeriğini HTML olarak ayrıştırın
soup = BeautifulSoup(response.content, "html.parser")

# Saatlik tahmin tablosunu bulun
table = soup.find("div", id="saatlikTahminDiv").find("table")  # id'yi değiştirdim

# Tablodaki tüm satırları bulun
rows = table.find_all("tr")

# Her satır için ilgili verileri seçin
data = []
for row in rows[1:]:
    cells = row.find_all("td")
    hour = cells[0].text.strip()
    temp = cells[1].text.strip()
    wind_speed = cells[6].text.strip()
    data.append([hour, temp, wind_speed])

# Verileri bir pandas DataFrame'e dönüştürün
df = pd.DataFrame(data, columns=["Saat", "Sıcaklık", "Rüzgar Hızı"])

# Verileri bir CSV dosyasına kaydedin
df.to_csv("istanbul_atasehir_saatlik_tahmin.csv", index=False)

# Verileri ekrana yazdırın
print(df)
