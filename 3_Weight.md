## Weight : Weight Matrix

#### Add Modules
<pre>
<code>
import pandas as pd
import numpy as np
from scipy.spatial import distance
</code>
</pre>

#### Make up Weighted Matrix for All Nodes
<pre>
<code>
filename = ['W0900', 'W0930', 'W1000', 'W1030', 'W1100', 'W1130', 'W1200', 'W1230', 'W1300']
sheetName = 'data'   # timestep 2 is 'W0900', ... , and 10 is 'W1300'

degree = 100
timestep = 10

TotalWeight = np.identity(degree)

for f in range(0, len(filename)):
    df = pd.read_excel(filename[f]+'.xlsx', sheet_name=sheetName)
    data = df[['PP', 'latitudeE7', 'longitudeE7']]

    Temp = np.identity(degree)
    for i in range(0, degree):

        if df.iloc[i][1] != 1:
            for j in range(0, degree):
                dst = distance.euclidean(df.iloc[i][1:3], df.iloc[j][1:3])
                if dst != 0:
                    Temp[i, j] = 1/dst**2
                    TotalWeight[i, j] = TotalWeight[i, j] + Temp[i, j]

print(TotalWeight)
</code>
</pre>

#### Make up Weighted Matrix for Contact Modeling
<pre>
<code>
sheetName = 'total'
df = pd.read_excel('../k-MeansClustering/100PP_GPS_Data_clustering_result.xlsx', sheet_name=sheetName)

print(df)

W = np.identity(degree)
snapshot = []
snapshot2 = []
for x in range(degree):
    snapshot2.append(99999)

input = df.iloc[1, 1]
print(input)

for i in range(1, timestep): # extract same cluster as input
    if i == 1:
        for j in range(0, degree):  # set non-input data to 0
            if input == df.iloc[j, i]:
                snapshot.append(df.iloc[j, i])
            else:
                snapshot.append(99999)
        snapshot2 = snapshot
        print('snapshot', i, ':', snapshot)
    else:
        for k in range(0, degree):
            if snapshot[k] != 99999:
                for l in range(0, degree):
                    if df.iloc[k, i] == df.iloc[l, i]:
                        snapshot2[l] = df.iloc[k, i]

    for k in range(0, degree):
        if snapshot2[k] != 99999:
            for l in range(0, degree):
                if k != l:
                    if snapshot2[k] == df.iloc[l, i]:
                        W[l, k] = TotalWeight[l, k]

print(W)

output = pd.DataFrame(W)
output.to_excel('weight.xlsx', index=False)
</pre>
</code>

#### Results

![weight](https://user-images.githubusercontent.com/66988643/87216934-20656400-c37f-11ea-81fe-386019795e6a.PNG)
