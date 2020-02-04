import numpy as np
import pickle
import os

X_test, y_test = np.load("X_test.npy",allow_pickle=True), np.load("y_test.npy",allow_pickle=True)

list_acc = []
for filename in os.listdir("model"):
    if (".sav" in filename):
        try:
            print(filename)
            clf = pickle.load(open("model/%s" % filename,"rb"))
            pred = clf.predict(X_test)
            from sklearn.metrics import accuracy_score
            acc = accuracy_score(y_test,pred)
            list_acc.append([filename,acc])
        except Exception as e:
            print (e)
import pandas as pd
pd.DataFrame(list_acc,columns=["Model","Accuracy"]).to_csv("result/Hasil_Train.csv",index=False)