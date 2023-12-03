"""
Utility Calcs for 3D rectangular sim
"""
import numpy as np
from lunarsats.three_dee import setup

mu_earth = setup.mu_earth

def accel(r_moon, r_sat, sat=False, debug=False) -> list:
    """
    Calculate forces on bodies
    """
    if sat is True:
        pass
        #delta_r = np.zeros(3)
        #delta_r_hat = np.zeros(3)
        #f_from_moon = np.zeros(3)
        #r_hat_earth = np.zeros(3)
        #f_from_earth = np.zeros(3)
        #delta_r = [r_sat[0] - r_moon[0],
        #           r_sat[1] - r_moon[1],
        #           r_sat[2] - r_moon[2]]
        #delta_r_hat = delta_r / np.linalg.norm(delta_r)
        #mag_delta_r = np.linalg.norm(delta_r)
        #force_mag_moon = G * mass_sat * mass_moon / (mag_delta_r)**2
        #f_from_moon = -force_mag_moon * delta_r_hat

        #r_hat_earth = r_sat / np.linalg.norm(r_sat)
        #force_mag_earth = G * mass_sat * mass_earth / (np.linalg.norm(r_sat))**2
        #f_from_earth = -force_mag_earth * r_hat_earth

        #return f_from_moon + f_from_earth  
    else:
        # Calculate force on moon (from Earth only, force from sat ~0)
        r_hat = np.zeros(3)
        f_from_earth = np.zeros(3)
        r_moon_mag = np.linalg.norm(r_moon)
        r_hat = r_moon / r_moon_mag
        if sat is False and debug is True:
            print(r_hat)

        force_mag = mu_earth / (r_moon_mag)**2
        f_from_earth = -force_mag * r_hat
        return f_from_earth
    
def rk4_sat(h, v, r_moon, r_sat):
    """
    Fourth-Order Runge-Kutta solver for Sat position and velocity
    """
    k11 = v
    k21 = accel(r_moon, r_sat, sat=True, debug=True)

    k12 = v + 0.5*h*k21
    k22 = accel(r_moon,r_sat+0.5*h*k11, sat=True)

    k13 = v + 0.5*h*k22
    k23 = accel(r_moon, r_sat+0.5*h*k12, sat=True)

    k14 = v + h*k23
    k24 = accel(r_moon, r_sat+h*k13, sat=True)

    position = r_sat + h * (k11 + 2.0*k12 + 2.0*k13 + k14) / 6.0
    velocity = v + h * (k21 + 2.0*k22 + 2.0*k23 + k24) / 6.0
    return [position, velocity]

    
def rk4_moon(h, v, r_moon, r_sat):
    """
    Fourth-Order Runge-Kutta solver for Moon position and velocity
    """
    k11 = v
    k21 = accel(r_moon, r_sat, debug=True)

    k12 = v + 0.5*h*k21
    k22 = accel(r_moon,r_sat+0.5*h*k11)

    k13 = v + 0.5*h*k22
    k23 = accel(r_moon, r_sat+0.5*h*k12)

    k14 = v + h*k23
    k24 = accel(r_moon, r_sat+h*k13)

    position = r_moon + h * (k11 + 2.0*k12 + 2.0*k13 + k14) / 6.0
    velocity = v + h * (k21 + 2.0*k22 + 2.0*k23 + k24) / 6.0
    return [position, velocity]