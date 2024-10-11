# © 2024 Numantic Solutions
# https://github.com/NMoroney
# MIT License
#

import sys
from sklearn.ensemble import IsolationForest

sys.path.insert(0, '../')
import mlc_utilities as mlc


print("mlcolor - isolation forest :")

path_zip = "../../data/"
name_zip = "mlcolor_blackgraywhite_rgbn.tsv.zip"

lines = mlc.zip_to_lines(path_zip, name_zip)

terms = ["black", "gray", "white"]

for term in terms:
    tab = "\t"
    matches = mlc.name_matches(term, lines, tab)

    rgbs, names = mlc.split_rgbn(matches, '\t')

    model = IsolationForest(n_estimators=100, max_samples='auto')
    model.fit(rgbs)
    predictions = model.predict(rgbs)

    if False :
        print (predictions)

    number_anomalies = 0
    ns = []
    for i, prediction in enumerate(predictions):
        if prediction == -1 :
            number_anomalies += 1
            ns.append(i)
        i += 1

    percent = float(number_anomalies) / float(len(rgbs))

    print("term              : " + term)
    print("number anomalies  : " + str(number_anomalies))
    print("percent anomalies : " + format(percent, '.2f'))
    print("rgbs[0]           : " + str(rgbs[0]))
    print("rgbs[-1]          : " + str(rgbs[-1]) + "\n")


