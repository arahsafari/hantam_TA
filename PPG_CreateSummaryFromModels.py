
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:45:31 2019

@author: cumitempur
"""
#from scipy.signal import argrelmax, argrelmin
import numpy as np 
from libraries import *
import os
from time import time

"""
Import classifier
"""
import pickle
clf = pickle.load(open("model/logistic_regression.sav","rb"))
"""
Generate Features and Classes
"""
daftar = []
for filename in os.listdir("fitur"):
    if (".csv" in filename):
        start = time()
        nomor = filename.replace(".csv","")
        print(nomor)
        try:
            feature_list, class_list = read_feature_from_csv("fitur/%s.csv" % nomor)
            daftar.append([nomor,feature_list,class_list])
        except Exception as e:
            print("failed",e)
            print(time() - start, "second")

"""
Export Result to CSV
"""
columns_list = ["Number", "Normal","PAC","PVC","pred_Normal", "pred_PAC","pred_PVC","tp_PAC","fp_PAC","tn_PAC","fn_PAC","acc_PAC","sp_PAC","sn_PAC","tp_PVC", "fp_PVC", "tn_PVC", "fn_PVC","acc_PVC","sp_PVC","sn_PVC"]
for filename in os.listdir("model"):
    if (".sav" in filename):
        try:
            print(filename)
            clf = pickle.load(open("model/%s" % filename,"rb"))
            hasil = []
            for data in daftar:
                feature_list = data[1]
                class_list = data[2]
                pred = clf.predict(feature_list)
                hasil.append(generate_confusion_matrix(data[0],class_list,pred,smoothing=False))        
            pd.DataFrame(hasil,columns=columns_list).to_csv("result/confusion_matrix_%s.csv" % filename.replace(".sav",""),index=False)
        except Exception as e:
            print(e)
            
