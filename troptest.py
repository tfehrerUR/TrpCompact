# -*- coding: utf-8 -*-
"""
@author: Tobi
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

xlim = [0,20000]
xmid = 2500
ipos = np.loadtxt('E0=3_frequency_data.dat', usecols=(0,5,6))
ineg = np.loadtxt('E0=-3_frequency_data.dat', usecols=(0,5,6))
mnum = np.where(ipos[:,0]==0)
iposhalved = ipos[int(mnum[0]):,:]
ineghalved = ineg[int(mnum[0]):,:]
arylgth = np.shape(iposhalved)[0]
tropism = np.empty((arylgth,2))
iposvals = np.empty((arylgth,1))
inegvals = np.empty((arylgth,1)) 

for i in range(arylgth):
    tropism[i,0] = iposhalved[i,0]
    iposvals[i,0] = iposhalved[i,1]+iposhalved[i,2]
    inegvals[i,0] = ineghalved[i,1]+ineghalved[i,2]
    tropism[i,1] = (iposvals[i,0] - inegvals[i,0])/(iposvals[i,0] + inegvals[i,0])

maxindpos = sig.find_peaks(iposvals[:,0])[0]
maxindneg = sig.find_peaks(inegvals[:,0])[0]
alp = np.shape(maxindpos)[0]
aln = np.shape(maxindneg)[0]
maxpos = np.empty((alp,2))
maxneg = np.empty((aln,2))
trp1 = np.empty((alp+aln,2))

for i, z in enumerate(maxindpos):
    maxpos[i,0] = tropism[z,0]
    maxpos[i,1] = iposvals[z,0]

for i, z in enumerate(maxindneg):
    maxneg[i,0] = tropism[z,0]
    maxneg[i,1] = inegvals[z,0]    

for i, z in enumerate(maxindpos):
    trp1[i,0] = tropism[z,0]
    trp1[i,1] = (iposvals[z,0]-inegvals[z,0])/(iposvals[z,0]+inegvals[z,0])

for i, z in enumerate(maxindneg):
    trp1[alp+i,0] = tropism[z,0]
    trp1[alp+i,1] = (iposvals[z,0]-inegvals[z,0])/(iposvals[z,0]+inegvals[z,0])

trp2 = np.sort(trp1, axis=0)

fig, axs = plt.subplots(2, 1)
axs[0].semilogy(maxpos[xlim[0]:xmid,0], maxpos[xlim[0]:xmid,1], color = 'blue', label = 'positive E0')
axs[0].semilogy(maxneg[xlim[0]:xmid,0], maxneg[xlim[0]:xmid,1], color = 'orange', label = 'negative E0')
axs[0].set_xlabel('HHG frequency in f/f0')
axs[0].set_ylabel('Intensity of maximum values')
axs[0].grid(True)
axs[0].legend(loc='upper right')

axs[1].scatter(trp1[xlim[0]:xmid,0], trp1[xlim[0]:xmid,1], s=5, color = 'blue', label = 'Local tropisms')
axs[1].set_xlabel('HHG frequency in f/f0')
axs[1].set_ylabel('Local tropisms')
axs[1].grid(True)
axs[1].legend(loc='upper right')

fig.suptitle('Evaluation of intensities and tropism effects')
fig.tight_layout()
plt.show()

