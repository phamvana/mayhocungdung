import pandas as pd
dulieu = pd.read_csv("baitap1.csv",delimiter = ',')

print("=============== Du lieu => 5 dong dau tien ========================")
print(dulieu.head())

print("=============== Du lieu => Tat ca cot thu 2 ========================")
print(dulieu.iloc[:,1:2])

print("=============== Du lieu => Dong thu 15 den 20 ========================")
print(dulieu.loc[14:21])

print("=============== Du lieu => cot 1 - 2 => Dong thu 15 ========================")
print(dulieu.iloc[15:16, 0:2])
