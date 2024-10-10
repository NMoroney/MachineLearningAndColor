# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import zipfile
import numpy as np
import colour


def zip_to_lines(path_zip, name_zip) :
    lines = []
    with zipfile.ZipFile(path_zip + name_zip) as archive :
        item = archive.read(name_zip[:-4])
        s = item.decode()
        lines = s.split('\n')
    return lines


def split_rgbn(lines, delimiter) :
    rgbs = []
    rs, gs, bs, names = [], [], [], []
    for line in lines :
        ts = line.split(delimiter)
        if len(ts) == 4 :
            rgbs.append([ int(ts[0]), int(ts[1]), int(ts[2]) ])
            names.append(ts[3])
    return rgbs, names


def to_classes(names):
    unique_names = list(set(names))

    to_index, to_name = {}, {}
    i = 0
    for name in unique_names :
        to_index[name] = i
        to_name[i] = name
        i += 1

    classes = []
    for name in names :
        classes.append(to_index[name])

    return unique_names, to_index, to_name, classes


def average_rgb(rgbs, bools):
    sum = [0.0, 0.0, 0.0]
    n = 0
    for i in range(len(rgbs)):
        rgb =rgbs[i]
        if bools[i]:
          sum[0] += rgb[0]
          sum[1] += rgb[1]
          sum[2] += rgb[2]
          n += 1
    nf = float(n)
    ave = [sum[0] / nf, sum[1] / nf, sum[2] / nf]
    return (ave[0] / 255.0, ave[1] / 255.0, ave[2] / 255.0)


def lightness_slice(min_, max_, n, lightness):
    x = np.linspace(min_, max_, n)
    y = np.linspace(min_, max_, n)

    aa, bb = np.meshgrid(x, y)

    ll = np.empty(aa.shape)
    ll.fill(lightness)

    return list(zip(ll.flatten(), aa.flatten(), bb.flatten()))


def radial_slice(lightness, chroma_step, hue_step):
    cn = np.linspace(1, 101, chroma_step)
    hn = np.linspace(0, 360, hue_step)

    cc, hh = np.meshgrid(cn, hn)

    ll = np.empty(cc.shape)
    ll.fill(lightness)

    lch = list(zip(ll.flatten(), cc.flatten(), hh.flatten()))
    return colour.LCHab_to_Lab(lch)


def a_star_slice(min_, max_, b_n, l_n, a_star):
    x = np.linspace(min_, max_, b_n)
    y = np.linspace(0, 100, l_n)

    bb, ll = np.meshgrid(x, y)

    aa = np.empty(bb.shape)
    aa.fill(a_star)

    return list(zip(ll.flatten(), aa.flatten(), bb.flatten()))


def b_star_slice(min_, max_, a_n, l_n, b_star):
    x = np.linspace(min_, max_, a_n)
    y = np.linspace(0, 100, l_n)

    aa, ll = np.meshgrid(x, y)

    bb = np.empty(aa.shape)
    bb.fill(b_star)

    return list(zip(ll.flatten(), aa.flatten(), bb.flatten()))


def in_srgb_gamut(labs):
    labs_in, srgbs_in = [], []
    for lab in labs:
        xyz = colour.Lab_to_XYZ(lab)
        srgb = colour.XYZ_to_sRGB(xyz)
        clipped = np.clip(srgb, 0, 1)
        if np.array_equal(srgb, clipped):
            labs_in.append(lab)
            srgbs_in.append(srgb)
    return np.array(labs_in), np.array(srgbs_in)

