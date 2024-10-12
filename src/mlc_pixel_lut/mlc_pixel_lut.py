# [2405]
#

import numpy as np
from sklearn.neighbors import KNeighborsClassifier    
import PIL
import PIL.Image  

import sys
sys.path.insert(0, '../')
import mlc_utilities as mlc


path_zip = "../../data/"
name_zip = "mlcolor_11_terms_min_670_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')
unique_names, to_index, to_name, classes = mlc.to_classes(names)

classes = []
for name in names :
  classes.append(to_index[name])


# use an arthmetic mean for color of the corresponding centroid
#
centroids = np.zeros( shape=(len(unique_names), 3), dtype=float )
counts = np.zeros( shape=(len(unique_names)), dtype=float )
for i in range(len(rgbs)) :
  k = classes[i]
  counts[k] += 1
  centroids[k] += rgbs[i]

print ('centroids - arithmetic mean :')
for i in range(len(centroids)) :
  centroids[i] /= counts[i]
  print ('  ' + to_name[i] + ' : ' + str(centroids[i]))


knn = KNeighborsClassifier(n_neighbors = 15)

knn.fit(rgbs, classes)

step = 4   # 4, 8, 16

vs = list(range(0, 257, step))
vs[-1] = 255

# create RGB LUT with 3D grid sampling of values
#
rgbs = []
for red in vs:
    for green in vs:
        for blue in vs:
            rgb = [red, green, blue]
            rgbs.append(rgb)

print(rgbs[:4])
print(rgbs[-4:])

# at each LUT pixel store the corresponding classifier prediction
#
qrgbs = []
j = 0
for rgb in rgbs:
    prediction = knn.predict( [(rgb[0], rgb[1], rgb[2])] )
    qrgb = list(centroids[prediction])
    qr = int(qrgb[0][0])
    qg = int(qrgb[0][1])
    qb = int(qrgb[0][2])
    qrgbs.append([qr, qg, qb])
    if j % 1000 == 0:
        print(j, end=" ", flush=True)
    j += 1
print()

print(qrgbs[:4])
print(qrgbs[-4:])

# save the resulting LUT as a PNG image
#
wide = len(vs)
high = wide * wide
img = PIL.Image.new(mode="RGB", size=(wide, high))

j = 0
for y in range(high):
    for x in range(wide):
        img.putpixel((x, y), (qrgbs[j][0], qrgbs[j][1], qrgbs[j][2]))
        j += 1

name_out = ("mlcolor_lut-knn-" + str(len(unique_names)) + "-" +
            str(wide) + "x" + str(wide) + "x" + str(wide) + ".png")

img.save(name_out)

