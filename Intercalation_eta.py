# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:10:35 2019

@author: Manik
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000
R = 8.314
T = 298.15
F = 96485

x = np.linspace(0.01,0.99,N)
f = 1;
i00 = 1e-3;
i = f;
j = 0

def f_i0(xs):
    return i00*(1-xs)**0.5*xs**0.5

i0 = [f_i0(xi) for xi in x];
eta_ch = [(2*R*T/F)*np.arcsinh(1/2*(i/i0_j)) for i0_j in i0]
eta_dch = [(2*R*T/F)*np.arcsinh(-1/2*(i/i0_j)) for i0_j in i0]
res_ch = [eta/i for eta in eta_ch]
res_dch = [eta/i for eta in eta_dch]
#plt.plot(x, eta_ch, x, eta_dch)
plt.xlabel("XLi")
plt.ylabel("Overpotential")
plt.plot(x, res_ch, x, res_dch)
plt.xlabel("XLi")
plt.ylabel("Resistance")
plt.show();