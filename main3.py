import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D

# Read lottery csv data and save to lottery_data variable
df = pd.read_csv("./data/new_lottery.csv")
lottery_data = [df["1"], df["2"], df["6"], df["bonus"], df["weather"]]

"""1st KMeans, first and second numbers cluster (K=3)"""
x, y = lottery_data[0], lottery_data[1]
X = list(zip(x, y))

# Calling sklearn KMeans, cluster where K=3
kmeans = KMeans(n_clusters=3).fit(X)
labels = kmeans.labels_

# Calling matplotlib, plot the graph
# x, y are 1st, 2nd lottery number for each.
# c is color. for clustered label
fig, ax = plt.subplots()
ax.scatter(x, y, c=labels.astype(np.float))
ax.grid(True)
ax.set_title("first and second number clusters (K=3)")
ax.set_xlabel("first")
ax.set_ylabel("second")
plt.savefig("./plot/first and second number.png", dpi=150)
plt.show()

"""2nd KMeans, bonus, sixth number and weather clusters (k=4)"""
x, y, z = lottery_data[2], lottery_data[3], lottery_data[4]
X = list(zip(x, y, z))

# Calling sklearn KMeans, cluster where K=4
kmeans = KMeans(n_clusters=4).fit(X)
labels = kmeans.labels_

# Calling matplotlib, plot the graph
# x, y, z are bonus, sixth number and weathers for each.
# c is color. for clustered label
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(x, y, z, c=labels.astype(np.float))
ax.grid(True)
ax.set_title("bonus, sixth number and weather clusters (K=4)")
ax.set_xlabel("bonus")
ax.set_ylabel("sixth")
ax.set_zlabel("weather")
plt.savefig("./plot/bonus, sixth number and weather.png", dpi=150)
plt.show()
