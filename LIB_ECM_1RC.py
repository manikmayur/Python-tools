# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:34:22 2019

@author: Manik
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))

filename = os.path.join(my_path, "LIB_data\A123_OCV.csv")
SOC, Voc = np.loadtxt(filename,comments='#',delimiter=',',usecols=(0,1),unpack=True)

filename = os.path.join(my_path, "LIB_data\A123_T25.csv")
t, step, I, V, chgAh, disAh = np.loadtxt(filename,comments='#',delimiter=',',usecols=(0,1,2,3,4,5),unpack=True)
OCV = interpolate.interp1d(SOC,Voc)

fig1, ax1 = plt.subplots()
ax1.plot(SOC, Voc)

Tau = 1.53
R1 = 0.0671
C1 = Tau/R1
R0 = 0.1203
Q = 2.055938009974541;
z = np.zeros(len(I))
iR1 = np.zeros(len(I))
V1 = np.zeros(len(I))
V2 = np.zeros(len(I))
def simCell(i,T,dT,z0,iR0,h0):
    # Compute output equation
    z[0] = z0
    iR1[0] = iR0
    V1[0] = OCV(z[0])
    V2[0] = OCV(z[0])
    for k in range(1, len(i)-1):
        if i[k]>0:
            eta = 0.95
        else:
            eta = 1
        RCfact = np.exp(-dT/(R1*C1))
        z[k] = z[k-1]-i[k-1]*eta*dT/(Q*3600)
        iR1[k] = RCfact*iR1[k-1]+(1-RCfact)*i[k-1]
        V1[k] = OCV(z[k])-i[k]*R0 #+ M*hk + M0*sik;
        V2[k] = OCV(z[k])-iR1[k]*R1-i[k]*R0 #+ M*hk + M0*sik;
    return V1, V2
#simCell(ik,T,deltaT,z0,iR0,h0)
V1, V2 = simCell(I,298.15,1,1,0,0)
tk = np.linspace(0,len(I),len(I))
fig2, ax2 = plt.subplots()
ax2.plot(tk, V1,'b-',tk, V2,'k-')
ax2.plot(tk, I,'r-')
plt.xlim((0,1500))
plt.ylim((0,4))