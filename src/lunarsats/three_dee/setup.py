"""
Setup for 3D rectangular coords
"""
# ================= TIMING =================
time_0 = 0
time_final = 100   # time, in Earth years
iter = 100 * time_final

# ================= NORMALIZATION =================
year2sec = 365 * 24 * 60 * 60
radius = 384.4e6    # Earth to Moon
mass_earth = 6e24

# ================= CONSTANTS =================
G = 6.674e-11   # N*m^2*kg^-2

# ================= MOON =================
mass_moon = 7.3477e22 #kg
r_moon = [radius, 0, 0] #meters
v_moon_mag = 1023 #m/s
v_moon = [0, v_moon_mag, 0]

# ================= SAT =================
sat_mass = 1000 #kg
r_sat = [384.4e6 + 1e6, 0, 0]
v_sat_mag = 1023*25
v_sat_mag = [0, v_sat_mag, 0]