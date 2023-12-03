"""
Setup for 3D rectangular coords
"""
import numpy as np
# ================= TIMING =================
time_0 = 0
time_final = 1   # time, in Earth days
iterations = 1 * time_final * 3600 * 24
h = 10 # fidelity. Less = more fine. [1, iterations]

t = np.linspace(time_0,time_final,iterations)
t[0] = time_0
r_sat = np.zeros([iterations, 3])
r_moon = np.zeros([iterations, 3])
v_sat = np.zeros([iterations, 3])
v_moon = np.zeros([iterations, 3])

# ================= NORMALIZATION =================

# ================= CONSTANTS =================
mu_earth = 398600 #km
# ================= MOON =================
r_moon_0 = [384400, 0, 0] #km
v_moon_mag = 1.01830 #km/s
v_moon_0 = [0, v_moon_mag, 0]

# ================= SAT =================
#mass_sat = 1 #kg
#r_sat_0 = [1.1, 0, 0]
#v_sat_mag = 1.1
#v_sat_0 = [0, v_sat_mag, 0.5]

# ================= Setup =================
#r_sat[0,:] = r_sat_0
r_moon[0,:] = r_moon_0
#v_sat[0,:] = v_sat_0
v_moon[0,:] = v_moon_0