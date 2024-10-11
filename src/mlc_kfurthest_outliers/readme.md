

## Machine Learning Color : K-Furthest Outliers

Look at thresholded k-furthest points (see also [mlpack's tutorial](https://github.com/mlpack/mlpack/blob/master/doc/tutorials/approx_kfn.md)) from centroid to flag possible outliers.

The furthest points are computed as the sorted inverse distances to the centroid.

The threshold or knee is computed with the [kneed](https://pypi.org/project/kneed/) library implementation of [kneedle](https://raghavan.usc.edu/papers/kneedle-simplex11.pdf) algorithm.

Below is result for a subset of RGBs labeled 'black' :

<img src="mlcolor_kfurthest_01.jpg" width=500px>

And a rough estimate of ~5% values above the knee.

```
mlcolor - k-furthest :
670
[31.86417910447761, 27.27313432835821, 29.992537313432837]
670
0.0039041140645855858
0.36408553983292846
633
percent above : 5.5223880597014885
```
