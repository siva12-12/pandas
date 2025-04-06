import pandas as pd
from sklearn.preprocessing import MinMaxScaler 

# Sample DataFrame
data = pd.read_csv('data.csv')
df = pd.DataFrame(data)

# Count null values per column
null_counts = df.isnull().sum()

data['Pulse'].fillna(data['Pulse'].mean(),inplace=True)
data['Duration'].fillna(data['Duration'].mean(),inplace=True)
data['Maxpulse'].fillna(data['Maxpulse'].mean(),inplace=True)
data['Calories'].fillna(data['Calories'].mean(),inplace=True)
null_counts = df.isnull().sum()
print(null_counts)
print(data)
max = data['Calories'].max()
min = data['Calories'].min()
print(max)
print(min)
column_name = "calories"
scaler = MinMaxScaler
df[["Calories"]] = scaler.fit_transform(data[["Calories"]])
print(data)