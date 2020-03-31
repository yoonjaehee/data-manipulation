import pandas as pd
data = pd.read_csv("C:\\Users\\ytjh0\\Desktop\\lottery.csv")
data2 = data.drop(["round","date"],axis=1)
data3=data2.apply(pd.value_counts).fillna(0).astype(int)
data3=data3.sum(axis=1)
print(data3.sort_values(ascending=False))
