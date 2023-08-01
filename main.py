# Havadurumu.xlsx dosyasını açmak için openpyxl modülünü içe aktarın
import openpyxl

# Dosyayı bir çalışma kitabı nesnesi olarak yükleyin
wb = openpyxl.load_workbook("datas/havadurumu.xlsx")

# İlk çalışma sayfasını alın
ws = wb[wb.sheetnames[0]]

# Çalışma sayfasındaki tüm satırları döngüye alın ve her satırın tüm hücrelerini ekrana yazdırın
# Sütunlar için ayrı ayrı hizalama yapmak için str.format () yöntemini kullanın
for row in ws.rows:
    print("{:<10} {:<10} {:>10} {:<10} {:^10} {:^10}".format(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, row[5].value))
