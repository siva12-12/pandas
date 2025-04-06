import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the CSV file
df = pd.read_csv("data.csv")

# Selecting the column to scale
scaler = MinMaxScaler()
df[["Maxpulse"]] = scaler.fit_transform(df[["Maxpulse"]])

print(df)
