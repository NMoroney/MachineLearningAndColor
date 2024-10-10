
## Machine Learning Color : Decision Tree

Use a [decision tree](https://scikit-learn.org/stable/modules/tree.html) [classifier](https://scikit-learn.org/dev/modules/generated/sklearn.tree.DecisionTreeClassifier.html) to classify input RGB data.

Classification report for the 11-color term data is below :

```
              precision    recall  f1-score   support

      yellow       0.87      0.90      0.88       199
       black       0.80      0.88      0.84       211
         red       0.83      0.80      0.82       235
       brown       0.73      0.65      0.69       226
        blue       0.85      0.85      0.85       233
      purple       0.81      0.71      0.76       243
       green       0.88      0.87      0.87       224
       white       0.83      0.82      0.82       230
      orange       0.76      0.75      0.76       215
        gray       0.76      0.81      0.78       210
        pink       0.72      0.80      0.76       207

    accuracy                           0.80      2433
   macro avg       0.80      0.80      0.80      2433
weighted avg       0.80      0.80      0.80      2433
```
