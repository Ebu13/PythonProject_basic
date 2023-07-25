import pandas as pd

# İlk20ecommercehacim.xlsx dosyasının adı ve yolunu ayarlayın
ecommerce_hacim_dosya = "datas/İlk20ecommercehacim.xlsx"

# Refah2021Endeksi.xlsx dosyasının adı ve yolunu ayarlayın
refah_endeksi_dosya = "datas/Refah2021Endeksi.xlsx"

# data/ecommercelink.xlsx dosyasının adı ve yolunu ayarlayın
ecommerce_link_dosya = "datas/ecommercelink.xlsx"

# İlk dosyayı DataFrame olarak okuyun
ecommerce_df = pd.read_excel(ecommerce_hacim_dosya)

# İkinci dosyayı DataFrame olarak okuyun
refah_df = pd.read_excel(refah_endeksi_dosya)

# Üçüncü dosyayı DataFrame olarak okuyun
ecommerce_link_df = pd.read_excel(ecommerce_link_dosya)

# Birleştirme işlemi
birlesik_df = ecommerce_df.merge(refah_df, left_on="Ülke", right_on="Ülke", how="inner")
birlesik_df = birlesik_df.merge(ecommerce_link_df, left_on="Ülke", right_on="Ülke", how="inner")

# Stil uygulayarak DataFrame'i güzel bir şekilde ekrana yazdır
birlesik_df = birlesik_df.style.format({'E-Ticaret Satış Hacmi (Milyar Dolar)': '{:.2f}'})
birlesik_df = birlesik_df.set_table_styles([{'selector': 'tr:hover', 'props': [('background-color', 'lightyellow')]}])

# DataFrame'in içeriğini ekrana yazdır
print(birlesik_df.data)

# Tabloyu Excel dosyasına kaydet
with pd.ExcelWriter('datas/view.xlsx') as writer:
    birlesik_df.to_excel(writer, index=False)
