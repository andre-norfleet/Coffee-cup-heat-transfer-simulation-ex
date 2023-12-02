import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp

def coffee_sys(t, X):
	
      temp = X[0]
	hns = X[1]
      hRs = X[2]
      hNv = X[3]
	hns = 1.31*(((temp - 21.8) / 0.0551955)**(.25))
	hRns = (-4*.924*5.67*10**(-8))*(( ((temp + 273) + (21.8+273)) / 2)**3)
      hNv = 1.35*((temp - 21.8) / .061)**(.25))
      hs = hns + hRns
      pV = ((10**5)/760)*( 10 ** (7.9668-(1668.21/(temp + 228)) ) )
      uW = ( (1/(hNv + hRns)) + (.002/(1*((.0512+.0551955)/2))) )**(-1)
      eFF = ( ((101325 - (.5*2493.39)) - (101325 - 2493.39))/(np.log( (101325-(.5*2493.39))/(101325 - 2493.39) )))
	return [dx_dt, dy_dt]
