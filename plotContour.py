# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:59:21 2019

@author: Manik
"""
import numpy as np
import matplotlib.pyplot as plt

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_concSLiAvg.dat"
t, i, x, CsAvg= np.loadtxt(filename,comments='#',usecols=(0,1,2,3),unpack=True)

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_concSLi.dat"
t, i, x, Cs= np.loadtxt(filename,comments='#',usecols=(0,1,2,3),unpack=True)

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_concElyte.dat"
t, i, x, Ce= np.loadtxt(filename,comments='#',usecols=(0,1,2,3),unpack=True)

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_Temperature.dat"
t, i, x, T= np.loadtxt(filename,comments='#',usecols=(0,1,2,3),unpack=True)

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_phiS.dat"
t, i, x, phiS= np.loadtxt(filename,comments='#',usecols=(0,1,2,3),unpack=True)
                        
filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_phiL.dat"
t, i, x, phiL= np.loadtxt(filename,comments='#',usecols=(0,1,2,3),unpack=True)

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outP2D_Vcell.dat"
tC, Vca, Van= np.loadtxt(filename,comments='#',usecols=(0,1,2),unpack=True)

xLen = 50;
tLen = 1001;

tr = np.unique(t)
xr = np.unique(x)

fig1, ax1 = plt.subplots()
CsAvgr = np.reshape(CsAvg,(xLen,tLen),order="F").T
CS = ax1.contourf(xr, tr, CsAvgr)
cbar = fig1.colorbar(CS)
ax1.set_title('CsAvg')
#
fig2, ax2 = plt.subplots()
Csr = np.reshape(Cs,(xLen,tLen),order="F").T
CS = ax2.contourf(xr, tr, Csr)
cbar = fig2.colorbar(CS)
ax2.set_title('Cs')
#
fig3, ax3 = plt.subplots()
Cer = np.reshape(Ce,(xLen,tLen),order="F").T
CS = ax3.contourf(xr, tr, Cer)
cbar = fig3.colorbar(CS)
ax3.set_title('Ce')
#
fig4, ax4 = plt.subplots()
Tr = np.reshape(T,(xLen,tLen),order="F").T
CS = ax4.contourf(xr, tr, Tr)
cbar = fig4.colorbar(CS)
ax4.set_title('T')
#
fig5, ax5 = plt.subplots()
phiSr = np.reshape(phiS,(xLen,tLen),order="F").T
CS = ax5.contourf(xr, tr, phiSr)
cbar = fig5.colorbar(CS)
ax5.set_title('phiS')
#
fig6, ax6 = plt.subplots()
phiLr = np.reshape(phiL,(xLen,tLen),order="F").T
CS = ax6.contourf(xr, tr, phiLr)
cbar = fig6.colorbar(CS)
ax6.set_title('phiL')

fig7, ax7 = plt.subplots()
plt.plot(tC,Vca-Van,'b-')
ax7.set_title('Vcell')

#plt.show();
