# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from sklearn import metrics

import sys
sys.path.insert(0, '../')
import mlcolor_utilities as mlc


path_zip = "../../data/"
name_zip = "mlcolor_redgreenyellow_n100_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')


km = KMeans( n_clusters = 3, init = 'random', n_init = 25, max_iter = 300)

labels = km.fit_predict(rgbs)

print(labels)
print(type(labels))
print(labels.shape)

to_index = {}
i = 0
for name in names:
  if name not in to_index:
    to_index[name] = i
    i += 1
labels_true = []
for name in names:
  labels_true.append(to_index[name])

print(str(labels_true) + "\n")

homogeneity  = metrics.homogeneity_score(labels_true, labels)
completeness = metrics.completeness_score(labels_true, labels)
v_measure    = metrics.v_measure_score(labels_true, labels) 
adj_rand_scr = metrics.adjusted_rand_score(labels_true, labels)
adj_mut_info = metrics.adjusted_mutual_info_score(labels_true, labels)
silh_score   = metrics.silhouette_score(rgbs, labels)

print("homogeneity                 : " + format(homogeneity, '.2f'))
print("completeness                : " + format(completeness, '.2f'))
print("v-measure                   : " + format(v_measure, '.2f'))
print("adjusted rand score         : " + format(adj_rand_scr, '.2f'))
print("adjusted mutual information : " + format(adj_mut_info, '.2f'))
print("silhouette score            : " + format(silh_score, '.2f'))

print()

