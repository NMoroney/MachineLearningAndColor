# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import sys
sys.path.insert(0, '../')
import mlcolor_utilities as mlc


print("mlcolor - centroid process :")

path_zip = "../../data/"
name_zip = "mlcolor_11_terms_min_670_rgbn.tsv.zip"

tab = '\t'
lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')
unique_names, to_index, to_name, classes = mlc.to_classes(names)

print(unique_names)

centroids = []
for name in unique_names:
    centroid = mlc.compute_centroid(name, rgbs, names)
    print(centroid)
    centroids.append(centroid)

term = "yellow"
idx = to_index[term]
patch = mlc.rgb_to_patch(centroids[idx], 250)
patch.save("mlc_patch_" + term + ".png")


matches = mlc.name_matches(term, lines, tab)
rgbs, names = mlc.split_rgbn(matches, tab)

p2 = mlc.rgbs_to_patch(rgbs, (255, 255, 255), 12)
p2.save("mlc_patch_" + term + "_rgbs.png")


images = []
for centroid in centroids:
    patch = mlc.rgb_to_patch(centroid, 64)
    images.append(patch)

row = mlc.row_paste(images)
row.save("mlc_centroids_patch.png")


images = []
for name in unique_names:
    matches = mlc.name_matches(name, lines, tab)
    rgbs, names = mlc.split_rgbn(matches, tab)
    patch = mlc.rgbs_to_patch(rgbs, (128, 128, 128), 4)
    images.append(patch)

r2 = mlc.row_paste(images)
r2.save("mlc_centroids_patch_rgbs.png")

