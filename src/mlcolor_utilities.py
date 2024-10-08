# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import zipfile


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


