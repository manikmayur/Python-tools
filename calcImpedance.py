# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 14:29:20 2019

@author: Manik
"""

import numpy as np
import matplotlib.pyplot as plt

Re = 1 # [Ohm]
Rct = 2 # [Ohm]
Cdl = 100e-6 # [F]
Aw = 1 # [Ohm/s^0.5]

def impWarburg(freq):
    zW = Aw/np.sqrt(2*np.pi*1j*freq)
    return zW

def impCapacitor(freq):
    zC = 1/(2*np.pi*1j*freq*Cdl)
    return zC

def impResistor(R,f):
    zR = R
    return zR

def impRandals(f):
    zRe = impResistor(Re,f)
    zRct = impResistor(Rct,f)
    zC = impCapacitor(f)
    zW = impWarburg(f)
    zR = zRe + (zRct + zW)*zC/(zRct + zW + zC)
    return zR

freq = np.logspace(-1,6,50)
# Plotting
fig, ax = plt.subplots()
#
zR = [impRandals(f) for f in freq]
zr = [z.real for z in zR]
zi = [-z.imag for z in zR]
ax.plot(zr, zi,'bo', label='Aw=1')
#
Aw = 10
zR = [impRandals(f) for f in freq]
zr = [z.real for z in zR]
zi = [-z.imag for z in zR]
ax.plot(zr, zi,'ro', label='Aw=10')
#
Aw = 100
zR = [impRandals(f) for f in freq]
zr = [z.real for z in zR]
zi = [-z.imag for z in zR]
ax.plot(zr, zi,'go', label='Aw=100')
ax.axis([0,5,0,3])
ax.set(xlabel='Real Impedance  /  Ohm',
       ylabel='Imaginary Impedance  /  Ohm')
ax.legend()
fig.savefig('Impedance.png')
plt.show();