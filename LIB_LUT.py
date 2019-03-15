# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:41:30 2019

@author: Manik
"""
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Initialization file for demo ssc_lithium_cell_1RC.mdl. Demo
# based on T. Huria, M. Ceraolo, J. Gazzarri, R. Jackey. "High Fidelity
# Electrical Model with Thermal Dependence for Characterization and
# Simulation of High Power Lithium Battery Cells," IEEE International
# Electric Vehicle Conference, March 2012
#
# Copyright 2012 The MathWorks, Inc.


# Lookup Table Breakpoints

SOC_LUT = np.array([0,0.1,0.25,0.5,0.75,0.9,1])
Temperature_LUT = np.array([5,20,40]) + 273.15

SOC, T = np.meshgrid(SOC_LUT, Temperature_LUT)

# Em Branch Properties (OCV, Capacity)

# Battery capacity
Capacity_LUT = np.array([28.0081,27.6250,27.6392]) #Ampere*hours

# Em open-circuit voltage vs SOC rows and T columns
Em_LUT = np.array([[3.4966,3.5057,3.5148],
                   [3.5519,3.5660,3.5653],
                   [3.6183,3.6337,3.6402],
                   [3.7066,3.7127,3.7213],
                   [3.9131,3.9259,3.9376],
                   [4.0748,4.0777,4.0821],
                   [4.1923,4.1928,4.1930]]) #Volts

E = interpolate.interp2d(Temperature_LUT,SOC_LUT,Em_LUT)
#E = interpolate.RectBivariateSpline(SOC_LUT,Temperature_LUT,Em_LUT)
fig, ax = plt.subplots()
ax.plot(SOC_LUT, E(5+273.15,SOC_LUT), 'b-', label='T=5')
ax.plot(SOC_LUT, E(20+273.15,SOC_LUT),'r-', label='T=20')
ax.plot(SOC_LUT, E(40+273.15,SOC_LUT),'k-', label='T=40')
#ax2.plot(V, I)
ax.legend()
plt.xlabel("SOC")
plt.ylabel("E")
plt.show();

# Terminal Resistance Properties

# R0 resistance vs SOC rows and T columns
R0_LUT = np.array([[0.0117,0.0085,0.0090],
                   [0.0110,0.0085,0.0090],
                   [0.0114,0.0087,0.0092],
                   [0.0107,0.0082,0.0088],
                   [0.0107,0.0083,0.0091],
                   [0.0113,0.0085,0.0089],
                   [0.0116,0.0085,0.0089]]) #Ohms

# RC Branch 1 Properties

# R1 Resistance vs SOC rows and T columns
R1_LUT = np.array([[0.0109,0.0029,0.0013],
                   [0.0069,0.0024,0.0012],
                   [0.0047,0.0026,0.0013],
                   [0.0034,0.0016,0.0010],
                   [0.0033,0.0023,0.0014],
                   [0.0033,0.0018,0.0011],
                   [0.0028,0.0017,0.0011]]) #Ohms

# C1 Capacitance vs SOC rows and T columns
C1_LUT = np.array([[1913.6,12447,30609],
                   [4625.7,18872,32995],
                   [23306,40764,47535],
                   [10736,18721,26325],
                   [18036,33630,48274],
                   [12251,18360,26839],
                   [9022.9,23394,30606]]) #Farads