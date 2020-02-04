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

import matplotlib.pyplot as plt

"""
Main Program
"""
nomor = 212
ppg_signal, ppg_class = annotation_to_ppg_signal_labeled("data","annotation",nomor)


#LOAD SIGNAL FROM NPY
#signal = np.load("revisi/ppg_normal_sample.npy", allow_pickle=True)
#signal = np.load("revisi/ppg_pac_sample.npy", allow_pickle=True)
signal = np.load("revisi/ppg_pvc_sample.npy", allow_pickle=True)
sample_rate = 500



#test = ppg_signal[:,1]
#signal_a = []
#for i in range(1):
#    signal_a.append(ppg_signal[i])



#filtered = signal

#test_qt = feature_extraction_qt(signal_a , preprocess=True)

#TIME DOMAIN FEATURE
#import math
#features_time_domain = []
##for signal in signal_a:
#filtered = preprocess_ppg_signal(signal)
#r_peaks = find_signal_peaks(filtered,minimum=0.2)
#rr_list, rr_startstop = get_rr(r_peaks,to_sec=True,sample_rate=sample_rate)
#
#rata_ppi = np.mean(rr_list)
#std_ppi = np.std(rr_list)
#rata_sinyal = np.mean(filtered)
#std_sinyal = np.std(filtered)
#
#if(math.isnan(rata_ppi) or math.isnan(std_ppi) or math.isnan(rata_sinyal) or math.isnan(std_sinyal)):
#    print("TRUE")
#else:
#    features_time_domain.append([rata_ppi,std_ppi,rata_sinyal,std_sinyal])
#    
#sinyal_peak = [filtered[peak] for peak in r_peaks]
#plt.plot(filtered)
#plt.scatter(r_peaks,sinyal_peak,c='red')
#END TIME DOMAIN FEATURE


#SLIDING WINDOW
#from itertools import *
#features_time_domain = []
#window_count = 3
##for signal in signal_a:
#filtered = preprocess_ppg_signal(signal)
#r_peaks = find_signal_peaks(filtered,minimum=0.2)
#rr_list, rr_startstop = get_rr(r_peaks,to_sec=True,sample_rate=sample_rate)
#middle = int(len(rr_list)/2)
#kiri = middle-(window_count//2)
#rr_list = rr_list[kiri:kiri+window_count].tolist()
#rr_startstop = rr_startstop[kiri:kiri+window_count]
#
##flatten arraynya
#rubahke1d = list(chain.from_iterable(rr_startstop))
#sinyal_peak = [filtered[peak] for peak in rubahke1d]
#plt.plot(filtered)
#plt.scatter(rubahke1d,sinyal_peak,c='red')
#END SLIDING WINDOW



#QT INTERVAL
#second = secondDerivative(signal)
#filtered = preprocess_ppg_signal(second)
#filtered *= 10**10
#r_peaks = find_signal_peaks(filtered,minimum=0.2)
#qt_list, qt_startstop = detect_qt(r_peaks,to_sec=True,sample_rate=500)
#
#
#index_qnya = []
#index_tnya = []
#for index_p in qt_startstop:
#    index_qnya.append(index_p[0])
#    index_tnya.append(index_p[1])
#    
#
#sinyal_peak = [filtered[peak] for peak in r_peaks]
#sinyal_q = [filtered[peak] for peak in index_qnya]
#sinyal_t = [filtered[peak] for peak in index_tnya]
#
#
#
#plt.plot(filtered[50:4200])
##plt.plot(second[50:4200])
#
#plt.scatter(r_peaks,sinyal_peak,c='red')
#plt.scatter(index_qnya,sinyal_q,c='green')
#plt.scatter(index_tnya,sinyal_t,c='blue')
#
#plt.show()
#END QT INTERVAL

#SKENARIO 2
#TIME DOMAIN AND SLIDING WINDOW
#import math
#features_time_domain = []
#window_count = 6
##for signal in signal_a:
#filtered = preprocess_ppg_signal(signal,sample_rate=sample_rate)
#r_peaks = find_signal_peaks(filtered,minimum=0.2)
#rr_list, rr_startstop = get_rr(r_peaks,to_sec=True,sample_rate=sample_rate)
#
#rata_ppi = np.mean(rr_list)
#std_ppi = np.std(rr_list)
#rata_sinyal = np.mean(filtered)
#std_sinyal = np.std(filtered)
#
#middle = int(len(rr_list)/2)
#kiri = middle-(window_count//2)
#rr_list = rr_list[kiri:kiri+window_count].astype("float64")
#rr_startstop = rr_startstop[kiri:kiri+window_count]
#
##test_array = [0 for i in range(window_count)]
#
#if(math.isnan(rata_ppi) or math.isnan(std_ppi) or math.isnan(rata_sinyal) or math.isnan(std_sinyal)):
#    print("TRUE")
#else:
#    array_1 = [rata_ppi,std_ppi,rata_sinyal,]
#    array_1.extend(rr_list)
##    array_1.extend(test_array)
#    features_time_domain.append(array_1)
#std_sinyal
#kiri = 3
#r_peaks = r_peaks[kiri:kiri+window_count]    
#sinyal_peak = [filtered[peak] for peak in r_peaks]
#plt.plot(filtered)
#plt.scatter(r_peaks,sinyal_peak,c='red')




#TIME DOMAIN AND QT INTERVAL
#features = []
#window_count=6
#second = secondDerivative(signal)
#signal = preprocess_ppg_signal(second,sample_rate=sample_rate)
#signal *= 10**10
#
#peaks = find_signal_peaks(signal,minimum=0.2)
#qt_list, qt_startstop = detect_qt(peaks,to_sec=True,sample_rate=sample_rate)
#
#index_qnya = []
#index_tnya = []
#middle = int(len(qt_list)/2)
#kiri = middle-(window_count//2)
#for index_p in qt_startstop[kiri:kiri+window_count]:
#    index_qnya.append(index_p[0])
#    index_tnya.append(index_p[1])
#
#rata_qt = np.mean(qt_list)
#std_qt = np.std(qt_list)
#rata_sinyal = np.mean(signal)
#std_sinyal = np.std(signal)
#        
#
#middle = int(len(qt_list)/2)
#kiri = middle-(window_count//2)
#qt_list = qt_list[kiri:kiri+window_count].astype("float64")
#        
#
#if(math.isnan(rata_qt) or math.isnan(std_qt) or math.isnan(rata_sinyal) or math.isnan(std_sinyal)):
#  print("TRUE")
#  
#  rata_qt = np.nansum(np.mean(qt_list))
#  std_qt = np.nansum(np.std(qt_list))
#  rata_sinyal = np.nansum(np.mean(signal))
#  std_sinyal = np.nansum(np.std(signal))
#  if (len(qt_list) == window_count):
#      array_1 = [rata_qt,std_qt,rata_sinyal,std_sinyal]
#      array_1.extend(qt_list)
#      features.append(array_1)
#  
##          features.append([rata_qt,std_qt,rata_sinyal,std_sinyal]+qt_list)
#  
#else:
#    if (len(qt_list) == window_count):
#        array_1 = [rata_qt,std_qt,rata_sinyal,std_sinyal]
#        array_1.extend(qt_list)
#        features.append(array_1)
#                
#        
#sinyal_peak = [signal[peak] for peak in peaks]
#sinyal_q = [signal[peak] for peak in index_qnya]
#sinyal_t = [signal[peak] for peak in index_tnya]      
#
#plt.plot(signal[50:4200])
##plt.scatter(peaks,sinyal_peak,c='red')
#plt.scatter(index_qnya,sinyal_q,c='green')
#plt.scatter(index_tnya,sinyal_t,c='blue')
#
#plt.show()
#END SKENARIO 2





#SKENARIO 3
#TIME DOMAIN AND SLIDING WINDOW AND QT
features = []
window_count = 6
second = secondDerivative(signal)
signal = preprocess_ppg_signal(second,sample_rate=sample_rate)
signal *= 10**10
        
peaks = find_signal_peaks(signal,minimum=0.2)
rr_list, rr_startstop = get_rr(peaks,to_sec=True,sample_rate=sample_rate)
qt_list, qt_startstop = detect_qt(peaks,to_sec=True,sample_rate=sample_rate)


#        SLIDING WINDOW
middle = int(len(rr_list)/2)
kiri = middle-(window_count//2)
sliding_window = rr_list[kiri:kiri+window_count].astype("float64")

#QT            
middle = int(len(qt_list)/2)
kiri = middle-(window_count//2)
qt_list = qt_list[kiri:kiri+window_count].astype("float64")

#        TIME DOMAIN
rata_ppi = np.mean(sliding_window)
std_ppi = np.std(sliding_window)
rata_qt = np.mean(qt_list)
std_qt = np.std(qt_list)
rata_sinyal = np.mean(signal)
std_sinyal = np.std(signal)

if(math.isnan(rata_ppi) or math.isnan(std_ppi) or math.isnan(rata_qt) or math.isnan(std_qt) or math.isnan(rata_sinyal) or math.isnan(std_sinyal)):
  print("TRUE")
  rata_ppi = np.nansum(np.mean(sliding_window))
  std_ppi = np.nansum(np.std(sliding_window))
  rata_qt = np.nansum(np.mean(qt_list))
  std_qt = np.nansum(np.std(qt_list))
  rata_sinyal = np.nansum(np.mean(signal))
  std_sinyal = np.nansum(np.std(signal))
  if (len(sliding_window) == window_count and len(qt_list) == window_count):
      array_1 = [rata_ppi,std_ppi,rata_qt,std_qt,rata_sinyal,std_sinyal]
      array_1.extend(sliding_window)
      array_1.extend(qt_list)
      features.append(array_1)
#          features.append([rata_ppi,std_ppi,rata_qt,std_qt,rata_sinyal,std_sinyal]+sliding_window+qt_list)
  
else:
    if (len(sliding_window) == window_count and len(qt_list) == window_count):
        array_1 = [rata_ppi,std_ppi,rata_qt,std_qt,rata_sinyal,std_sinyal]
        array_1.extend(sliding_window)
        array_1.extend(qt_list)
        features.append(array_1)
                














































#    plt.savefig("sinyal_clean_peaks",dpi=1000)



#second = secondDerivative(signal)
#signal = preprocess_ppg_signal(second)
#signal *= 10**10
#peaks = find_signal_peaks(signal,minimum=0.2)


#second = secondDerivative(signal)
#sinyal_bersih = preprocess_ppg_signal(second)
#sinyal_bersih *= 10**10
#peaks = find_signal_peaks(sinyal_bersih,minimum=0.2,freq=500)
#rr_list, rr_startstop = get_rr(peaks,to_sec=True,sample_rate=sample_rate)


#qt interval

    
        
#fitur3 = fitur_ekstraksi_qt_interval(ppg_signal)



#print(fitur3)





#peakss = [sinyal_bersih[peak] for peak in peaks]
#peak_qt =  [sinyal_bersih[peak] for peak in peaks]
#plt.plot(sinyal_bersih)
#plt.scatter(peaks,peakss,c='red')
#plt.scatter(peak_pertama,sinyal_peak_pertama,c='green')
#
##    plt.savefig("sinyal_clean_peaks",dpi=1000)
#plt.show()


#ppg_feature = feature_extraction_pp(ppg_signal,window_count=6,preprocess=False)
#for i in range(len(ppg_feature)):
#    ppg_feature[i].append(ppg_class[i])
#save_feature_to_csv("fitur",nomor,ppg_feature)


