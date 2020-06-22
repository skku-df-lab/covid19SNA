import matplotlib.pyplot as plt
import networkx as nx

import pandas as pd
import numpy as np

df = pd.read_excel('weight.xlsx')

degree = 100

IDW = np.identity(degree)
maximum = 0

# Find the maximum weight value
for i in range(0, degree):
    for j in range(0, degree):
        if i != j:
            if  df.iloc[i, j] >= maximum:
                maximum = df.iloc[i, j]

print("maximum :", maximum)

maximumPlus = maximum +1

for i in range(0, degree):
    for j in range(0, degree):
        if df.iloc[i, j] != 0:
            if i != j:
                df.iloc[i, j] = (maximum - df.iloc[i, j])
                df.iloc[i, j] = df.iloc[i, j]

print(df)

output = pd.DataFrame(df)
output.to_excel('IDEweight.xlsx', index=False)