import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

sheetName = '0900'
df = pd.read_excel('100PP_GPS_Data.xlsx', sheet_name=sheetName)
k = 20
print(df)

cluster_data = df[['latitudeE7', 'longitudeE7']]

k_means = KMeans(n_clusters = k)
k_means.fit(cluster_data)

centroids = k_means.cluster_centers_
print(centroids)

df['cluster_id'] = k_means.labels_

print(df)

df.to_excel(sheetName+'.xlsx', index=False)

plt.scatter(df['latitudeE7'], df['longitudeE7'], c=kmeans.labels_.astype(float), s=1000, alpha=0.3, cmap='jet')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=10)
plt.title('Clustering of the Suspected - 9:00 am')
plt.xlabel('latitude')
plt.ylabel('longitude')

plt.show()
