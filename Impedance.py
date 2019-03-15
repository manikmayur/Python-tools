# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 10:20:10 2019

@author: Manik
"""
import numpy as np
import matplotlib.pyplot as plt
from impedance.circuits import Randles, CustomCircuit
from impedance.plotting import plot_nyquist

randles = Randles(initial_guess=[.01, .005, .1, .001, 200])
randlesCPE = Randles(initial_guess=[.01, .005, .1, .9, .001, 200], CPE=True)

customCircuit = CustomCircuit(initial_guess=[.01, .005, .1, .005, .1, .001, 200],
                              circuit='R_0-p(R_1,C_1)-p(R_1,C_1)-W_1/W_2')

print(randles)

data = np.genfromtxt('exampleData.csv', delimiter=',')
frequencies = data[:,0]
Z = data[:,1] + 1j*data[:,2]

# keep only the impedance data in the first quandrant
frequencies = frequencies[np.imag(Z) < 0]
Z = Z[np.imag(Z) < 0]

randles.fit(frequencies, Z)
randlesCPE.fit(frequencies, Z)
customCircuit.fit(frequencies, Z)

print(customCircuit)

f_pred = np.logspace(5,-2)
randles_fit = randles.predict(f_pred)
randlesCPE_fit = randlesCPE.predict(f_pred)
customCircuit_fit = customCircuit.predict(f_pred)

fig, ax = plt.subplots(figsize=(5,5))

#randles.plot(frequencies, Z, CI=False)
#randlesCPE.plot(frequencies, Z, CI=False)
#customCircuit.plot(frequencies, Z, CI=True)

plot_nyquist(ax, frequencies, Z)
plot_nyquist(ax, f_pred, randles_fit)
plot_nyquist(ax, f_pred, randlesCPE_fit)
plot_nyquist(ax, f_pred, customCircuit_fit)

plt.show()