import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d') # Axe3D object

sheetName = 'total'
df = pd.read_excel('100PP_GPS_Data.xlsx', sheet_name=sheetName)

sample_size = 500
"""
x = np.cumsum(np.random.normal(0, 5, sample_size))
y = np.cumsum(np.random.normal(0, 5, sample_size))
z = np.cumsum(np.random.normal(0, 5, sample_size))
"""
x = df.latitudeE7[1:97]
y = df.PP[1:97]
z = df.longitudeE7[1:97]
ax.scatter(x, y, z, color='b', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[98:194]
y = df.PP[98:194]
z = df.longitudeE7[98:194]
ax.scatter(x, y, z, color='g', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[195:288]
y = df.PP[195:288]
z = df.longitudeE7[195:288]
ax.scatter(x, y, z, color='r', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[289:383]
y = df.PP[289:383]
z = df.longitudeE7[289:383]
ax.scatter(x, y, z, color='c', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[384:479]
y = df.PP[384:479]
z = df.longitudeE7[384:479]
ax.scatter(x, y, z, color='m', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[480:575]
y = df.PP[480:575]
z = df.longitudeE7[480:575]
ax.scatter(x, y, z, color='y', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[576:670]
y = df.PP[576:670]
z = df.longitudeE7[576:670]
ax.scatter(x, y, z, color='k', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[671:765]
y = df.PP[671:765]
z = df.longitudeE7[671:765]
ax.scatter(x, y, z, color='w', alpha=1, cmap=plt.cm.Greens)

x = df.latitudeE7[766:857]
y = df.PP[766:857]
z = df.longitudeE7[766:857]
ax.scatter(x, y, z, alpha=1, cmap=plt.cm.Greens)

plt.yticks(np.arange(900, 1300, 50), ["09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00"],
           fontsize=10,
           rotation=-15
           )

plt.savefig('180612_1225_3dplotting_scattering.svg')
plt.title("3D Scatter", color='b', fontsize=20)
plt.show()