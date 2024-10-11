# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import random
import sys

import numpy as np
import colour
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

sys.path.insert(0, '../')
import mlc_utilities as mlc


print("mlcolor : logistic regression")

path_zip = "../../data/"
name_zip = "mlcolor_blackgraywhite_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)

random.shuffle(lines)

tab = '\t'
matches = mlc.name_matches("black", lines, tab)
matches.extend(mlc.name_matches("gray", lines, tab))

rgbs, names = mlc.split_rgbn(matches, '\t')

names = [w.replace('black', '0') for w in names]
names = [w.replace('gray', '1') for w in names]
indices = [int(i) for i in names]

ls = []
for rgb in rgbs:
    srgb = [rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0]
    xyz = colour.sRGB_to_XYZ(srgb)
    lab = colour.XYZ_to_Lab(xyz)
    ls.append(lab[0])

xs = np.array([ls]).T
ys = np.array([indices]).T 
x_train, x_test, y_train, y_test = train_test_split(xs, ys, test_size=0.5, random_state=0)

clf = LogisticRegression(random_state=0)

clf.fit(x_train, y_train.ravel())

y_pred = clf.predict(x_test)

confusion = metrics.confusion_matrix(y_test, y_pred)
print (confusion)


y_pred_proba = clf.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.axis('equal')
plt.gca().set_aspect('equal', 'box')
plt.title("ROC Curve")

plt.savefig("mlc_logistic_roc_01.jpg")


print(clf.coef_, clf.intercept_)


plt.clf()


Xs = [i for i in range(80)]
Ys = [clf.predict_proba([[value]])[0][1] for value in range(80)]

threshold = 0.5
min_i = 0
min_d = abs(Ys[min_i] - threshold)
for i in range(len(Ys)) :
  diff = abs(Ys[i] - threshold)
  if diff < min_d :
    min_d = diff
    min_i = i

print ("min i : " + str(min_i))
print ("Xs min i : " + str(Xs[min_i]))
  
plt.scatter(xs, ys, color='#0000a010')
plt.plot(Xs, Ys, color='red')
plt.scatter(Xs[min_i], 0.5, color='gray', s=75)
plt.title("Logistic Regression : Black (0) vs Gray (1)")
plt.xlabel("Lightness or estimated L*")
plt.ylabel("Probability")

plt.savefig("mlc_logistic_prob_01.jpg")

