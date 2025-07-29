import seaborn as sns

tips = sns.load_dataset("tips") 
df= tips.copy()  # kopyalama

print(df.head()) # ilk 5 satır

df.info() #  sütun bilgileri

print(df.tail())  # son 5 satır

print(df.describe())  # sayısal sütunların istatistiksel bilgileri

print(df.describe().T)  # transpoze etme

df.rename(columns={"total_bill": "fiyat", "tip": "bahşiş", "sex": "cinsiyet", "smoker": "sigara", "time": "zaman",
                   "size": "kişiler"}, inplace=True)  # sütun adlarını değiştirme

print(df.head()) 
