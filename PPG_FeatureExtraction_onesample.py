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
import scipy.stats




"""
Main Program
"""
nomor = 437
ppg_signal, ppg_class = annotation_to_ppg_signal_labeled("data","annotation",nomor)
ppg_feature = feature_extraction_time_domain_features_and_sliding_window(ppg_signal,preprocess=True)
#ppg_feature = feature_extraction_pp(ppg_signal,window_count=6,preprocess=False)
#ppg_feature = feature_extraction_time_domain_features_and_sliding_window_and_qt(ppg_signal,window_count=3,preprocess=True)




#
for i in range(len(ppg_feature)):
    ppg_feature[i].append(ppg_class[i])
#save_feature_to_csv("fitur",nomor,ppg_feature)


