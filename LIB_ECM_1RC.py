# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:34:22 2019

@author: Manik
"""

import numpy as np
from scipy import interpolate, optimize
import matplotlib.pyplot as plt
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))

filename = os.path.join(my_path, "LIB_data\A123_OCV_T25.csv")
C, Voc = np.loadtxt(filename,comments='#',delimiter=',',usecols=(0,1),unpack=True)

filename = os.path.join(my_path, "LIB_data\A123_T25.csv")
t, step, I, V, chgAh, disAh = np.loadtxt(filename,comments='#',delimiter=',',usecols=(0,1,2,3,4,5),unpack=True)
                                         
SOC = 1 - C/np.max(C)
OCV = interpolate.interp1d(SOC,Voc)

Tau = 1.53
#R1 = 0.0671
#C1 = Tau/R1
#R0 = 0.1203
Q =  np.max(C)
tend = 1500 #1500
I = I[0:tend]
V = V[0:tend]
z = np.zeros(len(I))
iR1 = np.zeros(len(I))
V1 = np.zeros(len(I))
V2 = np.zeros(len(I))

# OCV with internal resistance model
def simCellR(i,R0,dt,z0,iR0,h0):
    # Compute output equation
    z[0] = z0
    V1[0] = OCV(z[0])
    for k in range(1, len(i)-1):
        if i[k]>0:
            eta = 0.95
        else:
            eta = 1
        z[k] = z[k-1]-i[k-1]*eta*dt/(Q*3600)
        V1[k] = OCV(z[k])-i[k]*R0 #+ M*hk + M0*sik;
    return V1

def simCellRC(i,R0,R1,C1,dt,z0,iR0,h0):
    # Compute output equation
    z[0] = z0
    iR1[0] = iR0
    V1[0] = OCV(z[0])
    for k in range(1, len(i)-1):
        if i[k]>0:
            eta = 0.95
        else:
            eta = 1
        RCfact = np.exp(-dt/(R1*C1))
        z[k] = z[k-1]-i[k-1]*eta*dt/(Q*3600)
        iR1[k] = RCfact*iR1[k-1]+(1-RCfact)*i[k-1]
        V1[k] = OCV(z[k])-iR1[k]*R1-i[k]*R0 #+ M*hk + M0*sik;
    return V1

#V1, V2 = simCell(I,298.15,1,1,0,0)
tk = np.linspace(0,len(I),len(I))

# Optimize parameters
def optim_R(I,R0):
    return simCellR(I,R0,1,1,0,0)

def optim_RC(I,R0,R1,C1):
    return simCellRC(I,R0,R1,C1,1,1,0,0)

par_R, params_covariance = optimize.curve_fit(optim_R, I, V,
                                               p0=[1])
par_RC, params_covariance = optimize.curve_fit(optim_RC, I, V,
                                               p0=[1,1,1])
# Plot results
fig1, ax1 = plt.subplots()
ax1.plot(SOC*100, Voc)
ax1.set_xlabel('SoC  /  %')
ax1.set_ylabel('Open Circuit Voltage  /  V')
plt.savefig("out_OCV.png")

fig2, ax2a = plt.subplots()
ax2b = ax2a.twinx()

V1 = optim_R(I,par_R[0])
V2 = optim_RC(I,par_RC[0],par_RC[1],par_RC[2])
ax2a.plot(tk, V,'k-',label='Expt')
ax2a.plot(tk, V1,'b--',label='R0')

ax2a.set_ylim([3.3,3.6])
plt.xlim((0,tend))
ax2a.set_xlabel('Time  /  s')
ax2a.set_ylabel('Voltage  /  V')
ax2a.legend()
#
color = 'red'
ax2b.plot(tk, I,color=color)
ax2b.set_ylim([0,1.5])
ax2b.set_ylabel('Current  /  A',color=color)
ax2b.tick_params(axis='y',labelcolor=color)
plt.savefig("out_R.png")
ax2a.plot(tk, V2,'g--',label='RC')
plt.savefig("out_RC.png")