# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import math
import PIL
import PIL.Image
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


def name_matches(query, lines, delimiter):
    matches = []
    for line in lines :
      ts = line.split(delimiter)
      if len(ts) > 3 :
        if ts[3] == query :
          matches.append(line)
    return matches


def compute_centroid(query, rgbs, names):
    sum_rgb = [ 0.0, 0.0, 0.0 ]
    n = 0.0
    for i, rgb in enumerate(rgbs) : 
        if names[i] == query:
            sum_rgb[0] += rgb[0]
            sum_rgb[1] += rgb[1]
            sum_rgb[2] += rgb[2]
            n += 1.0
    if n > 0: 
        centroid = [ sum_rgb[0] / n, sum_rgb[1] / n, sum_rgb[2] / n ]
    else:
        centroid = [ math.nan, math.nan, math.nan ]
    return centroid


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


def to_zip(lines, name_file):
    s = ""
    for line in lines:
        s += line + "\n"

    name_zip = name_file + '.zip'
    archive = zipfile.ZipFile(name_zip, 'w', compression=zipfile.ZIP_DEFLATED)
    archive.writestr(name_file, s)

