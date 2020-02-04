
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:45:31 2019

@author: cumitempur
"""
#from scipy.signal import argrelmax, argrelmin
import numpy as np 
from libraries import *
from time import time

"""
Generate Features and Classes
"""
feature_list, class_list = read_feature_from_csv("fitur_time_domain/219.csv")

"""
Import and fit classifier
"""
import pickle

clf = pickle.load(open("model/KNN_K7_time_domain.sav","rb"))
pred = clf.predict(feature_list)
count_train = class_count(class_list)
count_predict = class_count(pred)

"""
Training Metrics
"""
#from sklearn.metrics import *
#accuracy = accuracy_score(class_list,pred)
#precision = precision_score(class_list,pred,average="weighted")
#recall = recall_score(class_list,pred,average="weighted")
#hehe = generate_confusion_matrix(219,class_list,pred,smoothing=False)