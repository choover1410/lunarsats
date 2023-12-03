"""
3D Rectangular
"""
import numpy as np
import matplotlib.pyplot as plt
import lunarsats.utils.calc3D as calc3D
from lunarsats.three_dee import setup

def main():
    """
    3D Rectangular Main
    """
    h = setup.h
    iterations = setup.iterations
    r_sat = setup.r_sat
    v_sat = setup.v_sat
    r_moon = setup.r_moon
    v_moon = setup.v_moon
    print("===============")
    print(f"Moon r_0: {r_moon[0]}")
    print(f"Moon v_0: {v_moon[0]}")

    for t in range(0, iterations-1):
        #[r_sat[t+1,:], v_sat[t+1,:]] = calc3D.rk4_sat(h, v_sat[t,:], r_moon[t,:], r_sat[t,:])
        [r_moon[t+1,:], v_moon[t+1,:]] = calc3D.rk4_moon(h, v_moon[t,:], r_moon[t,:], r_sat[t,:])
        #print(r_sat[t+1,:])
              
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot()
    plt.scatter(r_moon[:,0], r_moon[:,1], s=2)
    ax.set_ylim(-400000, 400000)
    ax.set_xlim(-400000, 400000)

    plt.plot()
    plt.show()