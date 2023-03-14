import pandas as pd
dt = pd.read_csv("play_tennis.csv")
print("5 row first")
print(dt.head()) # 5 dong dau tien

print("----------------------")
print("7 row end")
print(dt.tail(7)) # 7 dong cuoi cung
print("----------------------")
print(" from row 3 to row 8")
print(dt.loc[3:8]) #dong thu3 den dong thu 8
print("----------------------")
print(" from column 3 to column 5")
print(dt.iloc[:,3:6])
print("----------------------")
print(" from row 5 - 9 of column 3")
print(dt.iloc[5:10, 3:4])
print("----------------------")
print("column Outlook")
print(dt.Outlook)


wine = pd.read_csv("wine.csv")
print(wine.head())