
## Machine Learning Color : K-Nearest Neighbors

Use the [k-nearest neighbor](https://scikit-learn.org/stable/modules/neighbors.html) [classifier](https://scikit-learn.org/dev/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) to classiy input RGB data.

Classification report for the 11-color term data is below :

```
              precision    recall  f1-score   support

      yellow       0.93      0.93      0.93       199
      purple       0.84      0.78      0.81       243
      orange       0.84      0.88      0.86       215
       black       0.86      0.94      0.90       211
        pink       0.80      0.84      0.82       207
       brown       0.87      0.78      0.82       226
        gray       0.78      0.89      0.83       210
       white       0.93      0.87      0.89       230
       green       0.96      0.91      0.93       224
        blue       0.89      0.91      0.90       233
         red       0.88      0.85      0.87       235

    accuracy                           0.87      2433
   macro avg       0.87      0.87      0.87      2433
weighted avg       0.87      0.87      0.87      2433
```
