"""
Setup for 3D rectangular coords
"""
import numpy as np
# ================= TIMING =================
time_0 = 0
time_final = 100   # time, in Earth years
iterations = 1 * time_final

# ================= NORMALIZATION =================
year2sec = 365 * 24 * 60 * 60
radius = 384.4e6    # Earth to Moon
mass_earth = 1

# ================= CONSTANTS =================
G = 1   # N*m^2*kg^-2

# ================= MOON =================
r_moon = np.zeros(3)
v_moon = np.zeros(3)

mass_moon = 1 #kg
r_moon = [1, 0, 0] #meters
v_moon_mag = 1 #m/s
v_moon = [0, v_moon_mag, 0]

# ================= SAT =================
r_sat = np.zeros(3)
v_sat = np.zeros(3)

mass_sat = 1 #kg
r_sat = [1.1, 0, 0]
v_sat_mag = 1.1
v_sat = [0, v_sat_mag, 0.5]