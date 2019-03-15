#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import Guo as Guo

#filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outSPMT.dat"
#t, xC, xA, T, VC, VA = np.loadtxt(filename,comments='#',usecols=(0,1,2,3,4,5),unpack=True)

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\outSPM.dat"
t, xC, xA, VC, VA = np.loadtxt(filename,comments='#',usecols=(0,1,2,3,4),unpack=True)

#Vcell_1C = VC_1C - VA_1C
Vcell = VC - VA

#phi_p0 = [phi0pos(xi) for xi in xC_1C];
mSPM = sio.loadmat('SPM_1C.mat')
def mat2np(name):
    val = mSPM[name]
    val = np.array([val[i][0] for i in range(len(val))])
    return val

mxp = mat2np('xp_s')
mxn = mat2np('xn_s')
mUC = mat2np('UC')
mUCca = mat2np('UC_ca')
mUCan = mat2np('UC_an')
mUGuo = mat2np('UGuo')
mt = mat2np('t')

lenX = len(mxp)
# Cell potential from Guo 2011 model
UGuoM = np.zeros(lenX)
UGuo_caM = np.zeros(lenX)
UGuo_anM = np.zeros(lenX)
for i in range(lenX):
    U,U_ca,U_an = Guo.fGetU_Guo(mxp[i],mxn[i])
    UGuoM[i] = U
    UGuo_caM[i] = U_ca
    UGuo_anM[i] = U_an
#
lenX = len(xC)
# Cell potential from Guo 2011 model
UGuo = np.zeros(lenX)
UGuo_ca = np.zeros(lenX)
UGuo_an = np.zeros(lenX)
for i in range(lenX):
    U,U_ca,U_an = Guo.fGetU_Guo(xC[i],xA[i])
    UGuo[i] = U
    UGuo_ca[i] = U_ca
    UGuo_an[i] = U_an   
#
fig1, ax1 = plt.subplots()
ax1.plot(t, xC, mt, mxp)

fig2, ax2 = plt.subplots()
ax2.plot(t, xA, mt, mxn)

fig3, ax3 = plt.subplots()
ax3.plot(mt,mUC,'bo',mt,mUGuo,'r-',t,Vcell,'kx')

fig4, ax4 = plt.subplots()
ax4.plot(mt,mUCca,'bo',mt,UGuo_caM,'r-',t,VC,'kx')

fig5, ax5 = plt.subplots()
ax5.plot(mt,mUCan,'bo',mt,UGuo_anM,'r-',t,VA,'kx')

fig6, ax6 = plt.subplots()
ax6.plot(t,T-273.15,'b-')

ax4.xlabel("Time")
ax4.ylabel("XLi")
plt.show();