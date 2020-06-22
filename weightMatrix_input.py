import pandas as pd
import numpy as np
from scipy.spatial import distance


############################################################
#####   Make up weighted Matrix for All Nodes  #####
############################################################

filename = ['W0900', 'W0930', 'W1000', 'W1030', 'W1100', 'W1130', 'W1200', 'W1230', 'W1300']
sheetName = 'data'

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

############################################################
#####   Make up weighted Matrix for Contact Modeling  #####
############################################################
sheetName = 'total'
df = pd.read_excel('../k-MeansClustering/100PP_GPS_Data_clustering_result.xlsx', sheet_name=sheetName)

print(df)

W = np.identity(degree)
snapshot = []
snapshot2 = []
for x in range(degree):
    snapshot2.append(999)

input = df.iloc[1, 1]
print(input)

for i in range(1, timestep): # input 과 동일한 클러스터를 추출
    if i == 1:
        for j in range(0, degree):  # input 외 데이터는 0으로 설정
            if input == df.iloc[j, i]:
                snapshot.append(df.iloc[j, i])
            else:
                snapshot.append(999)
        snapshot2 = snapshot
        print('snapshot', i, ':', snapshot)
    else:
        for k in range(0, degree):
            if snapshot[k] != 999:
                for l in range(0, degree):
                    if df.iloc[k, i] == df.iloc[l, i]:
                        snapshot2[l] = df.iloc[k, i]

    for k in range(0, degree):
        if snapshot2[k] != 999:
            for l in range(0, degree):
                if k != l:
                    if snapshot2[k] == df.iloc[l, i]:
                        W[l, k] = TotalWeight[l, k]

print(W)

output = pd.DataFrame(W)
output.to_excel('weight.xlsx', index=False)