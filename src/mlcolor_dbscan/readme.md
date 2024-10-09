
## Machine Color Learning : DBSCAN Clustering

For input human labeled red, green and blue values the [DBSCAN algorithm](https://scikit-learn.org/dev/modules/generated/sklearn.cluster.DBSCAN.html) is used to cluster the data.

[DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) is an abbreviation for "Density-based spatial clustering of applications with noise".

As a pre-processing step a [standard scaler](https://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.StandardScaler.html) is applied. 

The resulting first and second channels (originally red and green) are shown plotted below for the input data :


