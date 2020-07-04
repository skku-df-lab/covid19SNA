## Weight : WeightMatrix_input.py

#### 모든 노드들에 대한 각각의 가중치를 정방행렬(모든 노드 수(degree)X 모든 노드 수(degree))로 표현하는 작업 
<pre>
<code>
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
</code>
</pre>
