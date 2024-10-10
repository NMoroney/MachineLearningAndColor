
## Machine Learning : Radial SVM

Use the radial [Support Vector Machine (SVM)](https://scikit-learn.org/stable/modules/svm.html) [classifier](https://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html) to classify input RGB data.

Classification report for the 11-color term data is below :

```
              precision    recall  f1-score   support

      orange       0.85      0.89      0.87       215
         red       0.87      0.88      0.88       235
      purple       0.86      0.79      0.82       243
      yellow       0.96      0.92      0.94       199
       green       0.97      0.93      0.95       224
       brown       0.90      0.81      0.85       226
       black       0.86      0.96      0.91       211
        blue       0.88      0.92      0.90       233
        pink       0.86      0.86      0.86       207
       white       0.92      0.89      0.90       230
        gray       0.80      0.87      0.84       210

    accuracy                           0.88      2433
   macro avg       0.88      0.88      0.88      2433
weighted avg       0.88      0.88      0.88      2433
```

The corresponding confusion matrix for this classifer can be [seen here](https://github.com/NMoroney/MachineLearningColor/tree/main/src/mlcolor_confusionmatrix).

The above results can be compared to those from a [linear SVM](/src/mlcolor_linearsvm/).
