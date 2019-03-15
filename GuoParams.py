# -*- coding: utf-8 -*-

import numpy as np

# Parameter values taken from COMSOL single particle model file.
# Ref: Guo White 2011 JECS
# Electrochemistry: i_j = kj(T)*csmax_j*ce^0.5*xsurf_j^0.5*(1 ?
# xsurf_j)^0.5*[exp(0.5*F*eta_j/(RT) ? exp(0.5*F*eta_j/(RT)]

# Cell constants
F = 96487 # [C/mol] "Faraday constant"
R = 8.3143 # [J/(mol.K)] "Gas constant"
I1C = 1.656 # [A] "1C discharge current"
Tref = 298.15 # [K] "Reference temperature"

# Cell user input
T = 298.15 # [K] "Temperature
cR = 2 # [1] "C-Rate"
Iapp = - cR*I1C # [A] "Applied current - Discharge"
#Iapp = par.cR*par.I1C; % [A] "Applied current - Charge"

# Cell geometric parameters
Lsep = 25e-6 # [m] "Separator thickness"
Lca = 70e-6 # [m] "Cathode thickness"
Lan = 73.5e-6 # [m] "Anode thickness"
Lcell = Lsep+Lca+Lan # [m] "Cell thickness"

# Cathode material parameters
# Material: LCO
# References: 
rP_ca = 8.5e-6 #[m] "Particle radius cathode"
xLimax_ca = 1 # "Maximum cathode stoichiometry"
xLimin_ca = 0.4952 # "Minimum cathode stoichiometry"
DLiref_ca = 1e-14 # [m^2/s] "Solid phase Li-diffusivity LMO"
Ediff_ca = 29 # [kJ/mol] "Cathode diffusion activation energy"
def DLi_ca(T):
    DLi = DLiref_ca*np.exp(Ediff_ca/R*(1/T-1/Tref)) # [m^2/s] "Solid phase Li-diffusivity LMO"
    return DLi
csMax_ca = 51410 # [mol/m^3] "Max solid phase concentration cathode"
S_ca = 1.1167 # [m^2] "Cathode area"
Ltpb_ca = 2e5 # [m] "Cathode three phase boundary length"

# Anode material parameters
# Material: Graphite
# References: Guo Newman 2004 JECS 151, p. 1530; Kumaresan White 2008 JECS 155, p. A164; Gerver Meyers 2011 JECS 158, p. A83; Thomas Newman JPS 119-121, p. 844.

rP_an = 12.5e-6 # [m] "Particle radius anode"
xLimax_an = 0.7522 # [1] "Maximum anode stoichiometry"
xLimin_an = 0.01 # [1] "Minimum cathode stoichiometry"
DLiref_an = 3.9e-14 # [m^2/s] "Solid phase Li-diffusivity LMO"
Ediff_an = 35 # [kJ/mol] "Anode diffusion activation energy"
def DLi_an(T):
    DLi_an= DLiref_an*np.exp(Ediff_an/R*(1/T-1/Tref)) # [m^2/s] "Solid phase Li-diffusivity LMO"
    return DLi_an
csMax_an = 31833 # [mol/m^3] "Max solid phase concentration anode"
S_an = 0.7824 # [m^2] "Anode area"
Ltpb_an = 2e8 # [m] "Anode three phase boundary length"

# Electrolyte material parameters
cE = 1000 # [mol/m^3] "Electrolyte concentration"
cE_ref = 1000 # [mol/m^3] "Electrolyte reference concentration"

theta1 = (-5.636e-7*Iapp - 7.283e-6)*(Tref - 273.15)**3\
    +(5.676e-5*Iapp + 6.453e-4)*(Tref - 273.15)**2\
    +(-2.221e-3*Iapp - 1.635e-2)*(Tref - 273.15)+(2.437e-2*Iapp + 1.428e-1)
    
theta2 = (-6.824e-6*Iapp + 1.372e-5)*(Tref - 273.15)**3\
    +(6.054e-4*Iapp - 1.216e-3)*(Tref - 273.15)**2\
    +(-1.497e-2*Iapp + 3.025e-2)*(Tref - 273.15)+(7.179e-2*Iapp - 1.456e-1)

Rel = theta1 + theta2*(T - Tref) # [ohm] "Electrolyte phase resistance in the cell

# Electrochemical paramteres
Ltpb_ref = 1e5 # [m] "Reference electrode three phase boundary length"
Eact_an = 20 # [kJ/mol] "Anode activation energy"
Eact_ca = 58 # [kJ/mol] "Cathode activation energy"
# par.kref_an = 5.58e-10; % [m/s] "Anodic rate constant"
kref_an = 1.764e-11 # [m^2.5/(mol^0.5*s)] "Anodic rate constant" 
k_an = kref_an*np.exp(Eact_an/R*(1/T-1/Tref))
# par.kref_ca = 2.11e-9; % [m/s] "Cathodic rate constant"
kref_ca = 6.6667e-11 # [m^2.5/(mol^0.5*s)] "Cathodic rate constant"
k_ca = kref_ca*np.exp(Eact_ca/R*(1/T-1/Tref))
alpha_an = 0.5 # [1] "Symmetry factor anode"
alpha_ca = 0.5 # [1] "Symmetry factor cathode"
