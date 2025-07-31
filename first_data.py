import seaborn as sns

tips = sns.load_dataset("tips") 
df= tips.copy()  # kopyalama

print(df.head()) # ilk 5 satır

df.info() #  sütun bilgileri

print(df.tail())  # son 5 satır

print(df.describe())  # sayısal sütunların istatistiksel bilgileri

print(df.describe().T)  # transpoze etme

df.rename(columns={"total_bill": "fiyat", "tip": "bahşiş", "sex": "cinsiyet", "smoker": "sigara", "time": "zaman",
                   "size": "kişiler", "day": "gün"}, inplace=True)  # sütun adlarını değiştirme

print(df.head()) 

# Cinsiyet
df.cinsiyet.unique() # Cinsiyet sütunundaki benzersiz değerler

df["cinsiyet"] = df["cinsiyet"].map({"Female": "Kadın", "Male": "Erkek"}) # Cinsiyet sütunundaki değerleri değiştirme

# Sigara

print(df.sigara.unique()) # Sigara sütunundaki benzersiz değerler
df["sigara"] = df["sigara"].map({"No": "Hayır", "Yes": "Evet"}) # Sigara sütunundaki değerleri değiştirme

print(df.head())

#Gün

print(df.gün.unique()) # Gün sütunundaki benzersiz değerler

df["gün"]= df["gün"].map({"Thur": "Perşembe", "Fri": "Cuma", "Sat": "Cumartesi", "Sun": "Pazar"}) # Gün sütunundaki değerleri değiştirme

#zaman

print(df.zaman.unique()) # Zaman sütunundaki benzersiz değerler

df["zaman"] =df["zaman"].map({"Lunch":"Öğlen", "Dinner":"Akşam"}) # Zaman sütunundaki değerleri değiştirme

print(df.head()) # Değişiklikleri kontrol etme