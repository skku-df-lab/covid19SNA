## Weight : IDW (Inverse Distance Weighting)

#### 필요한 함수 모듈 추가
<pre>
<code>
import pandas as pd
import numpy as np
</code>
</pre>

#### 전체 가중치들 중 최대 가중치값을 찾는 작업
<pre>
<code>
df = pd.read_excel('weight.xlsx')

degree = 100

IDW = np.identity(degree)
maximum = 0

for i in range(0, degree):
    for j in range(0, degree):
        if i != j:
            if df.iloc[i, j] >= maximum:
                maximum = df.iloc[i, j]

print("maximum :", maximum)
</code>
</pre>

#### 역가중치 값을 구하는 작업
<pre>
<code>
maximumPlus = maximum +1

for i in range(0, degree):
    for j in range(0, degree):
        if df.iloc[i, j] != 0:
            if i != j:
                df.iloc[i, j] = (maximum - df.iloc[i, j])
                df.iloc[i, j] = df.iloc[i, j]
                
            ####df.iloc[i, j] = (maximumPlus - df.iloc[i, j])
            ####
            ####위 두줄 이렇게 바꿀 예정

print(maximumPlus)
print(df)

output = pd.DataFrame(df)
output.to_excel('IDEweight.xlsx', index=False)
</code>
</pre>
