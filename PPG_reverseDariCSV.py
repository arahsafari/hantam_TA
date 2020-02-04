#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:53:48 2019

@author: ipat
"""

import pandas as pd
from libraries import class_count

#def generateSignal(signal_file, anot_file):
#    signal = pd.read_csv(signal_file)
#    ecg, ppg = signal.iloc[1:,1], signal.iloc[1:,1]
 

#pd.np.save("ppg_pac_sample",ppg_pac[7])


nomor = "452"
signal_file = "data/%s.csv" % nomor
anot_file = "annotation/%s.csv" % nomor

signal = pd.read_csv(signal_file).replace("-",100)
annotation = pd.read_csv(anot_file)
ecg, ppg = signal.iloc[1:,1].values, signal.iloc[1:,2].values
uniq = annotation.groupby("signal_class").size()
hitung = class_count(annotation.signal_class.values)


ppg_normal, ppg_pac, ppg_pvc = [], [], []
ecg_normal, ecg_pac, ecg_pvc = [],[],[]
start, stop, signal_class = annotation["start_index"].values, annotation["stop_index"].values, annotation["signal_class"].values.tolist()
for i in range(len(annotation)):
    if (signal_class[i] == "N"):
        ppg_normal.append(ppg[start[i]:stop[i]].astype("float64"))
        ecg_normal.append(ecg[start[i]:stop[i]].astype("float64"))
    elif (signal_class[i] == "A"):
        ppg_pac.append(ppg[start[i]:stop[i]].astype("float64"))
        ecg_pac.append(ecg[start[i]:stop[i]].astype("float64"))
    elif (signal_class[i] == "V"):
        ppg_pvc.append(ppg[start[i]:stop[i]].astype("float64"))
        ecg_pvc.append(ecg[start[i]:stop[i]].astype("float64"))
