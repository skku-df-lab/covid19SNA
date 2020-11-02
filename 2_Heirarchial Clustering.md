## Heirarchial Clustering.py

#### Add Modules
<pre>
<code>
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as shc
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
</code>
</pre>

#### Heirarchial Clustering
<pre>
<code>
sheetName = '1300'
df = pd.read_excel('100PP_GPS_Data.xlsx', sheet_name=sheetName)
raw_data = df[['latitudeE7', 'longitudeE7']]
labels = df[['PP']]
clusters = 40

linked = linkage(raw_data, 'complete')

labelList = [labels.iloc[i, 0] for i in range(0, labels.size)]
"""
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', labels=labelList, distance_sort='descending', show_leaf_counts=True)
plt.title('Clustering of the Suspected - 09:30')
plt.show()
"""

cluster = AgglomerativeClustering(n_clusters=clusters, affinity='euclidean', linkage='complete')
cluster_labels = cluster.fit_predict(raw_data)

df['cluster_id'] = cluster_labels

print(df)

df.to_excel(sheetName+'.xlsx', index=False)
</pre>
</code>
