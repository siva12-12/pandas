import pandas as pd

data = {
    "bikes":["NS200","RC200","DUKE200"],
    "cars":["VOLKS","BMW","AUDI"]
}

var = pd.DataFrame(data)
print(var)
print(var.loc[0])

file = pd.read_csv('data.csv')
pd.options.display.max_rows = 99999 #Fix the limite
print(file.tail(5))

print("Helo Bhai")

print(file.head(15))

print("New wolrd")

print(file.info())