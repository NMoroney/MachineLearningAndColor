
## Machine Learning Color : Logistic Regression

Use logistic regression to train a black (0) or gray (1) classifier with lightness or L* data per label.

<img src="mlc_logistic_prob_01.png" width=500px>

Blue dots above are the data to train and test. The red data is the fitted classifer.

The gray dot is the 0.5 threshold or L* of ~32.

This example also computes a [Receiver Operating Characteristic](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html) ([ROC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)) curve.

<img src="mlc_logistic_roc_01.png" width=500px>
