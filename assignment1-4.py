import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
## ex1
# Read Data and save pick the first and second columns
data = pd.read_csv("C:\\Users\\ytjh0\\Desktop\\lottery.csv")
data2 = data.drop(["round","date","third","fourth","fifth","sixth","bonus"],axis=1)
# Making 3 Clusters 
clusters = KMeans(n_clusters=3).fit(data2)
# Making Graph
fig=plt.figure() # making form of plot
labels = clusters.labels_ 
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134) # showing in 3D
ax.scatter(data["first"],data["second"],c=labels.astype(np.float), edgecolor='k') # determine color and data's in graph
ax.set_xlabel('first') # set x label
ax.set_ylabel('second') # set y label
plt.show() # print the graph

## ex2
# Read Data and save pick the first~bounus columns and calculate mean of data
data3 = data.drop(["round","date","bonus"],axis=1)
data4 = data2.mean(axis=1)
data5 = data.drop(["round","date","first","second","fifth","sixth","bonus"],axis=1)
data5 = data5.mean(axis=1)
data6 = data.drop(["round","date","first","second","third","fourth","bonus"],axis=1)
data6 = data6.mean(axis=1)

# Madking 4 clusters
clusters = KMeans(n_clusters=4).fit(data3) # making clusters based on six numbers
# Making Graph
fig = plt.figure() # making form of plot
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134) # create plot object
ax.scatter(data4,data5,data6,c=labels.astype(np.float)) # using first-second, third-fourth, fifth-sixth means of numbers
ax.set_xlabel('mean of first & second number') # set x label
ax.set_ylabel('mean of third & fourth number') # set y label
ax.set_zlabel('mean of fifth & sixth number') # set z label
plt.show()
