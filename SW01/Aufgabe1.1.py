from pandas import Series,DataFrame
import pandas as pd

# Aufgaben 1.1
print("####### Aufgaben 1.1 #######")

# 1a)
data = pd.read_csv("child.csv", index_col=0)

# 1b)
print(data.shape)
print()

# 1c)
print("Mittelwert:")
print(data.mean())
print()
print("Median:")
print(data.median())
print()
