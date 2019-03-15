# -*- coding: utf-8 -*-
import numpy as np
import GuoParams as par

# Half cell potential from Guo, White 2011 JECS
def fGetU_Guo(xp,xn):
    mp = par.Iapp/(par.F*par.k_ca*par.S_ca*par.csMax_ca*par.cE**0.5*(1-xp)**0.5*xp**0.5)
    mn = -par.Iapp/(par.F*par.k_an*par.S_an*par.csMax_an*par.cE**0.5*(1-xn)**0.5*xn**0.5)

    # Calculate equilibrium half cell voltage
    Up_eq = Up_Tref(xp) + dUpdT(xp)*(par.T - par.Tref);
    Un_eq = Un_Tref(xn) + dUndT(xn)*(par.T - par.Tref);

    # Calculate activation overpotential
    etaAct_p = 2*par.R*par.T/par.F*np.log(0.5*(mp**2 + 4)**0.5 + 0.5*mp)
    etaAct_n = 2*par.R*par.T/par.F*np.log(0.5*(mn**2 + 4)**0.5 + 0.5*mn)

    # Calculate ohmic overpotential
    phil_p = par.Iapp*par.Rel;
    phil_n = 0;
    
    # Calculate half cell voltage
    Up = Up_eq + etaAct_p + phil_p;
    Un = Un_eq + etaAct_n + phil_n;

    UGuo = Up - Un;
    return UGuo, Up, Un

def Up_Tref(xp):
    Up_Tref = 4.04596 + np.exp(-42.30027*xp + 16.56714) \
    - 0.04880*np.arctan(50.01833*xp-26.48897)-0.05447*np.arctan(18.99678*xp-12.32362)\
    - np.exp(78.24095*xp-78.68074)
    return Up_Tref

def dUpdT(xp):
    dUpdT = 1e-3*(-0.19952+0.92837*xp-1.36455*xp**2+0.61154*xp**3)/\
    (1-5.66148*xp+11.47636*xp**2-9.82431*xp**3+3.04876*xp**4)
    return dUpdT

def Un_Tref(xn):
    Un_Tref = 0.13966+0.68920*np.exp(-49.20361*xn)+0.41903*np.exp(-254.40067*xn)\
    -np.exp(49.97886*xn-43.37888)-0.028221*np.arctan(22.52300*xn-3.65328)\
    -0.01308*np.arctan(28.34801*xn-13.43960)
    return Un_Tref

def dUndT(xn):
    dUndT = 1e-3*(0.00527+3.29927*xn-91.79326*xn**2+1004.91101*xn**3\
            -5812.27813*xn**4+19329.75490*xn**5-37147.89470*xn**6\
            +38379.18127*xn**7-16515.05308*xn**8)/\
            (1-48.09287*xn+1017.23480*xn**2-10481.80419*xn**3\
            +59431.30001*xn**4-195881.64880*xn**5+374577.31520*xn**6\
            -385821.16070*xn**7+165705.85970*xn**8)
    return dUndT

#UGuo, Up, Un = fGetU_Guo(0.6,0.3)