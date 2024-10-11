# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans

import sys
sys.path.insert(0, '../')
import mlc_utilities as mlc


path_zip = "../../data/"
name_zip = "mlcolor_redgreenyellow_n100_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')

xs = np.array([row[0] for row in rgbs])
ys = np.array([row[1] for row in rgbs])

plt.scatter(xs, ys, c = 'white', marker = 'o', edgecolor = 'black',  s = 50)
plt.axis('equal')
plt.title("K-means : Input Red, Green and Yellow Data")
plt.xlabel("Red")
plt.ylabel("Green")
plt.savefig("mlc_kmeans_xys.jpg")

plt.clf()


km = KMeans( n_clusters = 3, init = 'random', n_init = 25, max_iter = 300)

predictions = km.fit_predict(rgbs)

print(predictions)

print(type(predictions))
print(predictions.shape)

b0 = np.array([(value == 0) for value in predictions])
b1 = np.array([(value == 1) for value in predictions])
b2 = np.array([(value == 2) for value in predictions])

c0 = [mlc.average_rgb(rgbs, b0)]
c1 = [mlc.average_rgb(rgbs, b1)]
c2 = [mlc.average_rgb(rgbs, b2)]

plt.scatter(xs[b0], ys[b0], s = 75, c = c0, marker = 's', 
    edgecolor = 'black', label = 'cluster 1')
plt.scatter(xs[b1], ys[b1], s = 75, c = c1, marker = '^', 
    edgecolor = 'black', label = 'cluster 2')
plt.scatter(xs[b2], ys[b2], s = 75, c = c2, marker = 'o', 
    edgecolor = 'black', label = 'cluster 3')

plt.scatter(km.cluster_centers_[:, 0],  km.cluster_centers_[:, 1],
    s = 125, marker = 'D', c = 'cornflowerblue', 
    edgecolor = 'black', label = 'centroids')

plt.legend(scatterpoints=1)
plt.grid()
plt.title("K-means : red, green, yellow")
plt.xlabel("Red")
plt.ylabel("Green")
plt.axis('equal')
plt.savefig("mlc_kmeans_clustered.jpg")

