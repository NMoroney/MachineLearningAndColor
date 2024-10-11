# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import math
import zipfile

from kneed import KneeLocator   # https://pypi.org/project/kneed/

import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '../')
import mlc_utilities as mlc


print("mlcolor - k-furthest :")


def distances_wrt_centroid(query, rgbs, names):
    centroid = mlc.compute_centroid(query, rgbs, names)
    ds = []
    for i, rgb in enumerate(rgbs) :
        if names[i] == query:
            dr = centroid[0] - rgb[0]
            dg = centroid[1] - rgb[1]
            db = centroid[2] - rgb[2]
            dist = math.sqrt(float(dr * dr) + float(dg * dg) + float(db * db))
            ds.append(dist)
    return ds


path_zip = "../../data/"
name_zip = "mlcolor_blackgraywhite_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)

tab = '\t'
blacks = mlc.name_matches("black", lines, tab)
grays = mlc.name_matches("gray", lines, tab)
whites = mlc.name_matches("white", lines, tab)

print(str(len(blacks)))

rgbs, names = mlc.split_rgbn(blacks, tab)
# rgbs, names = mlc.split_rgbn(grays, tab)
# rgbs, names = mlc.split_rgbn(whites, tab)

term = "black"

centroid = mlc.compute_centroid(term, rgbs, names)
print(centroid)

ds = distances_wrt_centroid(term, rgbs, names)

inv_ds = [1.0 / d for d in ds]
inv_ds.sort()

print(str(len(inv_ds)))
print(inv_ds[0])
print(inv_ds[-1])

xs = range(0, len(inv_ds))

kneedle = KneeLocator(xs, inv_ds, S=1.0, curve="convex", direction="increasing")    # concave

kn = round(kneedle.knee, 3)
print(kn)

percent_above = 100.0 * (1.0 - float(kn) / float(len(inv_ds)))
print("percent above : " + str(percent_above))

plt.plot(xs, inv_ds)
x2 = [kn, kn]
y2 = [inv_ds[0], inv_ds[-1]]
plt.plot(x2, y2, linestyle = 'dashed')
plt.xlabel("sorted index value")
plt.ylabel("inverse distance")
plt.title("Knee (orange) of sorted inverse distances relative to centroid")

plt.savefig("mlc_kfurthest_01.jpg")
# plt.show()

