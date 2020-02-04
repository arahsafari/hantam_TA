# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 10:45:31 2019

@author: cumitempur
"""
from libraries import *
import numpy as np

"""
Main Program
"""
#Load Sinyal dari file buat tes
signal = np.load("ppg_pac_sample.npy", allow_pickle=True)[0]
#signal = pd.read_csv("data/485.csv").iloc[:,0]
#Koefisien Noise
mu, sigma = 0, 0.1 
#Generate Noise
noise = np.random.normal(mu, sigma, signal.shape) 
#Create Noisy Signal
noisy_signal = signal+noise
#Remove baseline using moving average
baseline_removed = baseline_remove_ppg(noisy_signal)
#Remove noise using DWT by removing high frequency si5gnal
clean_ppg = remove_noise(baseline_removed)
#Scale to 0-1
scaled = scaler.fit_transform(clean_ppg.reshape(-1,1))[:,0]
#Get Peaks
peaks = find_signal_peaks(scaled,minimum=0.4)
#Generate peak list
rr_list, rr_startstop = get_rr(peaks,to_sec=True,sample_rate=500)


import matplotlib.pyplot as plt
plt.plot(signal)
plt.savefig("sinyal_asli",dpi=1000)
plt.clf()
plt.plot(noisy_signal)
plt.savefig("sinyal_noisy",dpi=1000)
plt.clf()
plt.plot(clean_ppg)
plt.savefig("sinyal_clean",dpi=1000)
plt.clf()
plot_with_rpeaks(clean_ppg,peaks)