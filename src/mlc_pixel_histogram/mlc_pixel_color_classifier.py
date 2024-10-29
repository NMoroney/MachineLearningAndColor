# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import PIL
import PIL.Image  
import colour
import pandas as pd
import matplotlib.pyplot as plt


def counts_to_percents(counts):
    sum_ = float(sum(counts))
    percents = []
    for count in counts:
        percents.append(float(count) / sum_)
    return percents


def save_horizontal_stacked_bar_chart(name_jpg, names, percents, rgbs, show_legend):
    dict_ = { 'names' : names,
              'percents' : percents }

    df = pd.DataFrame.from_dict(dict_)

    df[['percents']].T.plot.barh(stacked=True,
                                 figsize=(8, 2),     # figsize=(15,2),
                                 color=rgbs,
                                 edgecolor='grey',
                                 legend=show_legend)

    plt.axis('off')
    plt.title("Pixel class histogram")
    if show_legend:
        plt.legend(df['names'].unique(), loc='lower center',
                   ncol = 6, bbox_to_anchor=(0.5, -0.2), frameon=False)

    plt.savefig(name_jpg)


def sort_indices(list_):
    copy = list_[:]
    sorted_list = sorted(copy)
    return [copy.index(i) for i in sorted_list]


print("mlc - pixel color classifer :")

path_lut = "../../data/"
name_lut = "mlcolor_lut-rsvm-17-65x65x65.png"

lut = PIL.Image.open(path_lut + name_lut)
w1 = lut.size[0]
print(lut.size)

path_img = "../mlc_pixel_color_classifier/"
img = PIL.Image.open(path_img + "Colorful_Bell_Peppers-512.JPG")

print(img.size)

classified = PIL.Image.new(mode="RGB", size=img.size)

wide, high = img.size[0], img.size[1]
for y in range(high) :
    print (y, end=' ', flush=True)
    for x in range(wide) :
        pixel = img.getpixel((x, y))
        rq = int(pixel[0] / 4)
        gq = int(pixel[1] / 4)
        bq = int(pixel[2] / 4)
        xq = bq
        yq = gq + (rq * w1)
        qrgb = lut.getpixel((xq, yq))
        classified.putpixel((x, y), (qrgb[0], qrgb[1], qrgb[2]))
print ('\n')

classified.save("Colorful_Bell_Peppers-512-classified.JPG")


dict_ = { }
for y in range(high) :
    for x in range(wide) :
        pixel = classified.getpixel((x, y))
        rgb = (pixel[0], pixel[1], pixel[2])
        if rgb in dict_:
            dict_[rgb] += 1
        else:
            dict_[rgb] = 1

lchs, cs, rgbs, ns, hue_lightness = [], [], [], [], []
i = 0
chroma_threshold = 5.0
for key, value in dict_.items():
    red = float(key[0]) / 255.0
    green = float(key[1]) / 255.0
    blue = float(key[2]) / 255.0
    srgb = (red, green, blue)
    xyz = colour.sRGB_to_XYZ(srgb)
    lab = colour.XYZ_to_Lab(xyz)
    lch = colour.Lab_to_LCHab(lab)
    if (lch[1] < chroma_threshold):
        lch[2] = 360 + lch[0]
    hue_lightness.append(lch[2])
    print(str(lch) + " : " + str(value))
    lchs.append(lch)
    cs.append(value)
    rgbs.append(srgb)
    ns.append(i)
    i += 1

sort_idx = sort_indices(hue_lightness)

print(sort_idx)

names, counts, nrgbs = [], [], []
for idx in sort_idx:
    names.append(str(ns[idx]))
    counts.append(cs[idx])
    nrgbs.append(rgbs[idx])

percents = counts_to_percents(counts)

show_legend = False
save_horizontal_stacked_bar_chart("mlc_pixel_class_histogram_01.jpg", names, percents, nrgbs, show_legend)

def sort_indices(list_):
    copy = list_[:]
    sorted_list = sorted(copy)
    
    return [copy.index(i) for i in sorted_list]

sort_idx = sort_indices(hue_lightness)



