# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import zipfile

from sklearn import svm

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

import matplotlib.pyplot as plt

import sys
sys.path.insert(0, '../')
import mlcolor_utilities as mlc


path_zip = "../../data/"
name_zip = "ml_color-11_terms-min_670-rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')
unique_names, to_index, to_name, classes = mlc.to_classes(names)

rgbs_train, rgbs_test, classes_train, classes_test = (
    train_test_split(rgbs, classes, test_size=0.33, random_state=42)
)

clf = svm.SVC(kernel='rbf')    # RBF is Radial Basis Functions

clf.fit(rgbs_train, classes_train)


predictions_test = clf.predict(rgbs_test)

class_labels = []
for i in range(len(unique_names)) :
  class_labels.append(to_name[i])

print(classification_report(classes_test, predictions_test, target_names=class_labels))

cm = confusion_matrix(classes_test, predictions_test, labels=clf.classes_)
print (cm)

disp = ConfusionMatrixDisplay.from_predictions(classes_test,
                                               predictions_test,
                                               cmap=plt.cm.Blues,
                                               display_labels=class_labels)

plt.xticks(rotation=90)
plt.title('Radial SVM : Confusion Matrix')
plt.savefig("mlcolor_confusionmatrix.png", bbox_inches='tight')

