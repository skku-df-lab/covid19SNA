## Weight : IDW (Inverse Distance Weighting)

#### Add Modules
<pre>
<code>
import pandas as pd
import numpy as np
</code>
</pre>

<pre>
<code>
df = pd.read_excel('weight.xlsx')

degree = 100

IDW = np.identity(degree)
maximum = 0
</code>
</pre>

#### Find the maximum weight value
<pre>
<code>
for i in range(0, degree):
    for j in range(0, degree):
        if i != j:
            if df.iloc[i, j] >= maximum:
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
</code>
</pre>

#### Results

![IDW](https://user-images.githubusercontent.com/66988643/87217147-560b4c80-c381-11ea-9e16-625bef6836e1.PNG)
