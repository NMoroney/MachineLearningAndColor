# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import math
import PIL
import PIL.Image

import sys
sys.path.insert(0, '../')
import mlcolor_utilities as mlc


def rgb_to_patch(rgb, dim_px):
    patch = PIL.Image.new(mode="RGB", size=(dim_px, dim_px))
    pixel = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    patch.paste(pixel, (0, 0, dim_px, dim_px))
    return patch


def rgbs_to_patch(rgbs, fill_rgb, n_upscale) :
    dim_px = int(math.sqrt(float(len(rgbs))) + 1) 
    patch = PIL.Image.new(mode="RGB", size=(dim_px, dim_px))
    patch.paste(fill_rgb, (0, 0, dim_px, dim_px))
    i = 0
    for y in range(dim_px) :
        for x in range(dim_px) :
            if i < len(rgbs):
                patch.putpixel((x, y), (rgbs[i][0], rgbs[i][1], rgbs[i][2]))
            i += 1
    wn = dim_px * n_upscale
    patch = patch.resize((wn, wn), PIL.Image.NEAREST)
    return patch


def row_paste(images):
    wide_in, high_in = images[0].size
    wide_out = len(images) * wide_in
    high_out = high_in
    row = PIL.Image.new(mode="RGB", size=(wide_out, high_out))
    row.paste((0, 0, 0), (0, 0, wide_out, high_out))

    all_equal = True
    for image in images:
        wn, hn = image.size
        if wn != wide_in or hn != high_in:
            all_equal = False
    assert all_equal, "row paste requires all input images to be of the same size."

    for i in range(len(images)):
        x = i * wide_in
        PIL.Image.Image.paste(row, images[i], (x, 0))
    return row


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

term = "yellow"   # orange
idx = to_index[term]
patch = rgb_to_patch(centroids[idx], 250)
patch.save("mlc_patch_" + term + ".png")


matches = mlc.name_matches(term, lines, tab)
rgbs, names = mlc.split_rgbn(matches, tab)

p2 = rgbs_to_patch(rgbs, (255, 255, 255), 12)
p2.save("mlc_patch_" + term + "_rgbs.png")


images = []
for centroid in centroids:
    patch = rgb_to_patch(centroid, 64)
    images.append(patch)

row = row_paste(images)
row.save("mlc_centroids_patch.png")


images = []
for name in unique_names:
    matches = mlc.name_matches(name, lines, tab)
    rgbs, names = mlc.split_rgbn(matches, tab)
    patch = rgbs_to_patch(rgbs, (128, 128, 128), 4)
    images.append(patch)

# images.append(rgb_to_patch((128,128,128), 32))

r2 = row_paste(images)
r2.save("mlc_centroids_patch_rgbs.png")

