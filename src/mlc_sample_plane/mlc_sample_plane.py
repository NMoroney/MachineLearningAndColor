# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import numpy as np
import colour
import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '../')
import mlc_utilities as mlc


print("mlcolor : sample plane")

slice_ = mlc.lightness_slice(-120, 120, 45, 65)
labs, srgbs = mlc.in_srgb_gamut(slice_)

plt.scatter(labs[:,1], labs[:,2], c=srgbs)
plt.xlabel('a*')
plt.ylabel('b*')
plt.title('CIELAB Lightness Slice')
plt.axis('equal')
plt.savefig("mlcolor_lightness_slice-01.jpg")

plt.clf()


slice_ = mlc.radial_slice(65, 25, 45)
labs, srgbs = mlc.in_srgb_gamut(slice_)

plt.scatter(labs[:,1], labs[:,2], c=srgbs)
plt.xlabel('a*')
plt.ylabel('b*')
plt.title('CIELAB Radial Slice')
plt.axis('equal')
plt.savefig("mlcolor_radial_slice-01.jpg")

plt.clf()


slice_ = mlc.a_star_slice(-120, 120, 50, 25, 0)
labs, srgbs = mlc.in_srgb_gamut(slice_)

plt.scatter(labs[:,2], labs[:,0], c=srgbs)
plt.xlabel('b*')
plt.ylabel('L*')
plt.title('CIELAB a* = 0 Slice')
plt.axis('equal')
plt.savefig("mlcolor_a_star_slice-01.jpg")

plt.clf()


slice_ = mlc.b_star_slice(-120, 120, 50, 25, 0)
labs, srgbs = mlc.in_srgb_gamut(slice_)

plt.scatter(labs[:,1], labs[:,0], c=srgbs)
plt.xlabel('a*')
plt.ylabel('L*')
plt.title('CIELAB b* = 0 Slice')
plt.axis('equal')
plt.savefig("mlcolor_b_star_slice-01.jpg")


