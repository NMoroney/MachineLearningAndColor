
## Machine Learning Color : Isolation Forest 

Use the [isolation forest](https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.IsolationForest.html) algorithm to identify possible outliers in black, gray and white labeled RGB data.

This analysis approximately 10% of data as being anomalous for this dataset.

```
mlcolor - isolation forest :
term              : black
number anomalies  : 60
percent anomalies : 0.09
rgbs[0]           : [9, 2, 21]
rgbs[-1]          : [19, 40, 55]

term              : gray
number anomalies  : 107
percent anomalies : 0.16
rgbs[0]           : [212, 209, 208]
rgbs[-1]          : [128, 113, 92]

term              : white
number anomalies  : 77
percent anomalies : 0.11
rgbs[0]           : [251, 252, 213]
rgbs[-1]          : [219, 206, 171]
```
