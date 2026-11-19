import matplotlib.pyplot as plt
import pandas as pd
import seaborn  as sns
df=pd.read_csv(r"C:\Users\cs\Desktop\Abubakar AIML\Iris.csv")
print(df)
print(df.info())
print(df.dropna(),inplace=True)
print(df.isnull().sum())
print(df.fillna(df.mean(numeric_only=True,inplace=True)))
print(df.isnull().sum())
