
## Machine Color Naming : Random Forest

Use the [random forest](https://scikit-learn.org/stable/modules/ensemble.html) [classifier](https://scikit-learn.org/dev/modules/generated/sklearn.ensemble.RandomForestClassifier.html) to classify input RGB data.

Classification report for the 11-color term data is below :

```
              precision    recall  f1-score   support

      orange       0.83      0.87      0.85       215
       green       0.95      0.94      0.94       224
      yellow       0.95      0.91      0.93       199
      purple       0.84      0.79      0.81       243
       black       0.87      0.95      0.91       211
        gray       0.81      0.87      0.83       210
       white       0.91      0.87      0.89       230
         red       0.86      0.86      0.86       235
        pink       0.82      0.83      0.82       207
       brown       0.87      0.77      0.82       226
        blue       0.86      0.91      0.89       233

    accuracy                           0.87      2433
   macro avg       0.87      0.87      0.87      2433
weighted avg       0.87      0.87      0.87      2433
```
These results can be compared to those from a [decision tree](/src/mlc_decision_tree).
