
## Machine Color Learning : Linear SVM

Use the [linear Support Vector Machine (SVM)](https://scikit-learn.org/stable/modules/svm.html) [classifier](https://scikit-learn.org/dev/modules/generated/sklearn.svm.LinearSVC.html) to classify input RGB data.

Classification report for the 11-color term data is below :

```
              precision    recall  f1-score   support

       black       0.68      0.98      0.80       211
         red       0.74      0.89      0.81       235
      yellow       0.90      0.95      0.93       199
       white       0.68      0.92      0.79       230
      orange       0.80      0.74      0.77       215
       green       0.96      0.90      0.93       224
       brown       0.76      0.43      0.55       226
        pink       0.76      0.79      0.77       207
        gray       0.71      0.55      0.62       210
      purple       0.87      0.58      0.69       243
        blue       0.83      0.90      0.86       233

    accuracy                           0.78      2433
   macro avg       0.79      0.78      0.77      2433
weighted avg       0.79      0.78      0.77      2433
```
