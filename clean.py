import pandas as pd

data = pd.read_csv('data.csv')
pd.options.display.max_rows = 9999


x= data["Maxpulse"].median()
data["Maxpulse"].fillna(x,inplace=True)
print(data)
data.isnull().sum()
print(data)