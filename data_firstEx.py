import seaborn as sns

tips = sns.load_dataset("tips")

df=tips.copy()  # kopyalama

print(df.head())

print(df.info())

print(df.tail())

print(df.describe())

print(df.describe().T)


df.rename(columns={"total_bill": "Fiyat", "tip": "Bahşiş", "sex": "Cinsiyet", "smoker": "Sigara", "time": "Zaman",
                   "size": "Kişiler", "day": "Gün"}, inplace=True)

print(df.head())