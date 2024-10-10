# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import zipfile
from io import StringIO
import pandas as pd

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
from sklearn import decomposition

print("mlcolor : principle components analysis :")

path_zip = "../../data/"
name_zip = "mlcolor_osa_uniform_color_scales_spectra.tsv.zip"

with zipfile.ZipFile(path_zip + name_zip) as archive :
    item = archive.read(name_zip[:-4])
    s = item.decode()
    tsv = StringIO(s)
    df = pd.read_csv(tsv, sep="\t", header=None, skiprows=1)

ns = range(0,5,1)
df.drop(df.columns[ns], axis=1, inplace=True)

if True:
    print(df)
    column_names = df.columns
    print(column_names)
    print(df.shape)

plt.cla()
pca = decomposition.PCA(n_components=3)

pca.fit(df)
p3d = pca.transform(df)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
 
ax.scatter(p3d[:,0], p3d[:,1], p3d[:,2], alpha=0.15)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.axis('equal')
ax.set_title("PCA : OSA Uniform Color Scales Spectra (36 dimensions) to 3D")

plt.show()    

