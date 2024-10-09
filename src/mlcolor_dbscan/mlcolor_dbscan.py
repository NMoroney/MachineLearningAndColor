# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

import sys
sys.path.insert(0, '../')
import mlcolor_utilities as mlc


path_zip = "../../data/"
name_zip = "mlcolor_redgreenyellow_n100_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')

rgbs_scaled = StandardScaler().fit_transform(rgbs)

xs = np.array([row[0] for row in rgbs_scaled])
ys = np.array([row[1] for row in rgbs_scaled])

plt.scatter(xs, ys, c = 'white', marker = 'o', edgecolor = 'black',  s = 50)
plt.axis('equal')
plt.title("K-means : Input Red, Green and Yellow Data")
plt.xlabel("Red")
plt.ylabel("Green")
plt.savefig("mlcolor_dbscan_xys.jpg")

plt.clf()


dbscan = DBSCAN(eps=0.65, min_samples=10).fit(rgbs_scaled)
labels = dbscan.labels_

number_clusters = len(set(labels)) - (1 if -1 in labels else 0)
number_noise = list(labels).count(-1)

print("number clusters     : " + str(number_clusters))
print("number noise points : " + str(number_noise))

bn = np.array([(value == -1) for value in labels])
b0 = np.array([(value ==  0) for value in labels])
b1 = np.array([(value ==  1) for value in labels])
b2 = np.array([(value ==  2) for value in labels])

c0 = [mlc.average_rgb(rgbs, b0)]
c1 = [mlc.average_rgb(rgbs, b1)]
c2 = [mlc.average_rgb(rgbs, b2)]

plt.scatter(xs[b0], ys[b0], s = 75, c = c0, marker = 's', 
    edgecolor = 'black', label = 'cluster 1')
plt.scatter(xs[b1], ys[b1], s = 75, c = c1, marker = '^', 
    edgecolor = 'black', label = 'cluster 2')
plt.scatter(xs[b2], ys[b2], s = 75, c = c2, marker = 'o', 
    edgecolor = 'black', label = 'cluster 3')
plt.scatter(xs[bn], ys[bn], s = 40, c = 'gainsboro', marker = 'o', 
    edgecolor = 'black', label = 'noise 3')

plt.legend(scatterpoints=1)
plt.grid()
plt.title("DBSCAN : red, green, yellow")
plt.xlabel("Red")
plt.ylabel("Green")
plt.axis('equal')
plt.savefig("mlcolor_dbscan_clustered.jpg")

