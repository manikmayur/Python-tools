#!/usr/bin/env python
import numpy as np 
import matplotlib.pyplot as plt

filename = "D:\Manik\Development\eclipse-MnM\BatterySim\myFile.txt"
t, CA, CB = np.loadtxt(filename, usecols=(0,1,2), unpack=True)
#t, CA, CB, V, I = numpy.loadtxt(filename, usecols=(0,1,2,3,4), unpack=True)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t, CA, 'bo',t, CB,'r-')
#ax2.plot(V, I)
plt.xlabel("Time")
plt.ylabel("XLi")
plt.show();