import seaborn as sns

tips = sns.load_dataset("tips")
df= tips.copy()

df.head()

df.info()


