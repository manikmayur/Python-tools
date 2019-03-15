# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

R = 8.314
T0 = 298.15

# Safari et al. Electrochem. Soc. 158 (2011) A562
def phi0neg(x):
    phi = 0.6379+0.5416*np.exp(-305.5309)+0.044*np.tanh(-(x-0.1958)/0.1088) \
    -0.1978*np.tanh((x-1.0571)/0.0854)-0.6875*np.tanh((x+0.0117)/0.0529) \
    -0.0175*np.tanh((x-0.5692)/0.0875)
    return phi

# Stewart et al. J. Electrochem. Soc. 155 (2008) A664
def phi0pos(y):
    phi = 6.0826-6.9922*y+7.1062*y**2-0.54549e-4*np.exp(124.23*y-114.2593) \
    -2.5947*y**3
    return phi

# Lundgren et al. J. Electrochem. Soc. 162 (2015) A413–A420
def diffEl(ce,T):
    D = 7.588e-11*np.exp(3536.9/R*(1/T0-1/T))*ce**2 \
    -3.036e-10*np.exp(3272/R*(1/T0-1/T))*ce \
    +3.654e-10*np.exp(8372.8/R*(1/T0-1/T))
    return D

# Lundgren et al. J. Electrochem. Soc. 162 (2015) A413–A420
def kappaEl(ce,T):
    k = 0.1147*np.exp(520/R*(1/T0-1/T))*ce**3 \
    -2.238*np.exp(1010/R*(1/T0-1/T))*ce**1.5 \
    +2.915*np.exp(1270/R*(1/T0-1/T))*ce
    return k

def dlnfdlnc(ce):
    val = (0.2731*ce**2+0.6352*ce+0.4577)/ \
    (0.1291*ce**3-0.3517*ce**2+0.4893*ce+0.5713-1)
    return val

x = np.linspace(0.01,0.99,N)

phi_n0 = [phi0neg(xi) for xi in x];
phi_p0 = [phi0pos(xi) for xi in x];

plt.plot(x, phi_n0, x, phi_p0)