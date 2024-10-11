# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import zipfile

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import sys
sys.path.insert(0, '../')
import mlc_utilities as mlc


path_zip = "../../data/"
name_zip = "mlcolor_11_terms_min_670_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)
rgbs, names = mlc.split_rgbn(lines, '\t')
unique_names, to_index, to_name, classes = mlc.to_classes(names)

rgbs_train, rgbs_test, classes_train, classes_test = (
    train_test_split(rgbs, classes, test_size=0.33, random_state=42)
)

clf = DecisionTreeClassifier(random_state=0)

clf.fit(rgbs_train, classes_train)


predictions_test = clf.predict(rgbs_test)

class_labels = []
for i in range(len(unique_names)) :
  class_labels.append(to_name[i])

print(classification_report(classes_test, predictions_test, target_names=class_labels))

