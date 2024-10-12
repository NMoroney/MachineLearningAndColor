
## Machine Learning Color : Pixel LUT

A practical consideration for machie learning of color is taking advantage of look up tables (or LUTs).

Pre-computing classifier results for a dense 3D sampling of RGB values yields a LUT which can be used to quickly classify pixels.

This code computes a 65 x 65 x 65 LUT for a K-nearest neighbor (with k = 17) and saves the result as a PNG image.
