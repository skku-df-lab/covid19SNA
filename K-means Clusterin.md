## K-MeansClustering.py 

#### 필요한 함수 모듈 추가
<pre>
<code>
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt  

</pre>
</code>

#### k-means clustering 함수를 이용하여 
#### K의 갯수를 지정한 후, 각 시간 간격별 데이터를 지정한 k값으로 그룹화하는 작업

<pre>
<code>
sheetName = '1230'
df = pd.read_excel('100PP_GPS_Data.xlsx', sheet_name=sheetName)
k = 20

print(df)

cluster_data = df[['latitudeE7', 'longitudeE7']]

kmeans = KMeans(n_clusters = k).fit(cluster_data)
centroids = kmeans.cluster_centers_
print(centroids)

df['cluster_id'] = kmeans.labels_

print(df)

df.to_excel(sheetName+'.xlsx', index=False)

plt.scatter(df['latitudeE7'], df['longitudeE7'], c=kmeans.labels_.astype(float), s=1000, alpha=0.3, cmap='jet')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=10)
plt.title('Clustering of the Suspected - 12:30')
plt.xlabel('latitude')
plt.ylabel('longitude')

plt.show()
</code>
</pre>
