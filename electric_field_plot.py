# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:20:36 2021

@author: Max
"""
import numpy as np
import matplotlib.pyplot as plt

E0      = 7
f       = 25
chirp_1 = -2
chirp_2 = 2
phase   = 0
sigma   = 35

t_end   = 80

def E(t,chirp,env,phase=0):
    return np.sin(2*np.pi*f*(1+chirp*t*1e-3)*t*1e-3+phase)*env

t = np.linspace(-t_end, t_end, num = 1000)

env = E0*np.exp(-t**2/sigma**2)


plt.close()
plt.clf()
plt.cla()
plt.scatter(t[::20],env[::20],color='grey',label='Envelope',s=1)
plt.scatter(t[::20],-env[::20],color='grey',s=1)
plt.plot(t,E(t,chirp_1,env,phase=phase),label=f"chirp={chirp_1}")
plt.plot(t,E(t,chirp_2,env,phase=phase),label=f"chirp={chirp_2}")
plt.grid()
plt.legend()
plt.xlabel('Time in fs')
plt.ylabel('Electric field E(t) in MV/cm')
plt.title(f"Electric field for CEP={phase}")
plt.show()
