"""
3D Rectangular
"""
import numpy as np
from lunarsats.three_dee import setup
import lunarsats.utils.calc3D as calc3D

def main():
    """
    3D Rectangular Main
    """
    t_i = setup.time_0
    t_f = setup.time_final
    iter = setup.iter
    t = np.linspace(t_i,t_f,iter)
    t[0] = t_i
    h = int((t_f - t_i)/iter)

    r_sat = np.zeros([iter, 3])
    r_moon = np.zeros([iter, 3])
    v_sat = np.zeros([iter, 3])
    v_moon = np.zeros([iter, 3])

    r_sat[0,:] = setup.r_sat
    r_sat[0,:] = setup.r_moon
    v_sat[0,:] = setup.v_sat
    v_sat[0,:] = setup.v_moon

    for t in range(0, iter-1):
        [r_sat[t+1,:], v_sat[t+1,:]] = calc3D.rk4(h, v_sat[t,:], r_moon[t,:], r_sat[t,:])
        [r_moon[t+1,:], v_moon[t+1,:]] = calc3D.rk4(h, v_moon[t,:], r_moon[t,:])
        print(r_sat[t+1,:], v_sat[t+1,:])
              