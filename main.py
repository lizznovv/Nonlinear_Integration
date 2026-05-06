import numpy as np
from System import Rossler_attractor
from Methods import *
from Graphs import *
from Error import *

def run_method(h, CT, method, trajectory, coefs):
    N = int(CT / h)

    for i in range(N):
        state = method(trajectory[-1], coefs, h)
        trajectory.append(state)


def main():
    CT = 200
    h = 0.01
    h10 = 0.001

    state = np.array([-0.7, -0.7, 1.0], float)

    traj_euler_h = [state]
    traj_ec_h = [state]
    traj_mid_h = [state]
    traj_vscd_h = [state]
    traj_rk4_h = [state]

    traj_euler_h10 = [state]
    traj_ec_h10 = [state]
    traj_mid_h10 = [state]
    traj_vscd_h10 = [state]
    traj_rk4_h10 = [state]

    coefs = np.array([0.2, 0.2, 5.7], float)

    run_method(h, CT, euler, traj_euler_h, coefs)
    run_method(h, CT, e_cromer, traj_ec_h, coefs)
    run_method(h, CT, midpoint, traj_mid_h, coefs)
    run_method(h, CT, vscd, traj_vscd_h, coefs)
    run_method(h, CT, rk4, traj_rk4_h, coefs)

    run_method(h10, CT, euler, traj_euler_h10, coefs)
    run_method(h10, CT, e_cromer, traj_ec_h10, coefs)
    run_method(h10, CT, midpoint, traj_mid_h10, coefs)
    run_method(h10, CT, vscd, traj_vscd_h10, coefs)
    run_method(h10, CT, rk4, traj_rk4_h10, coefs)
    """
    plot_projections(traj_euler_h, "Euler")
    #plot_3d(traj_euler_h, "Euler")
    plot_projections(traj_ec_h, "Euler-Cromer")
    #plot_3d(traj_ec_h, "Euler-Cromer")
    plot_projections(traj_mid_h, "Midpoint")
    # plot_3d(traj_midpoint_h, "Midpoint")
    plot_projections(traj_vscd_h, "VSCD")
    #plot_3d(traj_vscd_h, "VSCD")
    plot_projections(traj_rk4_h, "RK4")
    #plot_3d(traj_rk4_h, "RK4")
    
    plot_projections(traj_euler_h10, "Euler")
    # plot_3d(traj_euler_h10, "Euler")
    plot_projections(traj_ec_h10, "Euler-Cromer")
    # plot_3d(traj_ec_h10, "Euler-Cromer")
    plot_projections(traj_mid_h10, "Midpoint")
    # plot_3d(traj_midpoint_h10, "Midpoint")
    plot_projections(traj_vscd_h10, "VSCD")
    # plot_3d(traj_vscd_h10, "VSCD")
    plot_projections(traj_rk4_h10, "RK4")
    # plot_3d(traj_rk4_h10, "RK4")
    """

    error_euler_h = error_calculation(traj_euler_h, traj_rk4_h)
    error_euler_h10 = error_calculation(traj_euler_h10, traj_rk4_h10)
    plot_error_two_steps(error_euler_h, error_euler_h10, h, "Euler vs RK4")

    error_ec_h = error_calculation(traj_ec_h, traj_rk4_h)
    error_ec_h10 = error_calculation(traj_ec_h10, traj_rk4_h10)
    plot_error_two_steps(error_ec_h, error_ec_h10, h, "Euler-Cromer vs RK4")

    error_mid_h = error_calculation(traj_mid_h, traj_rk4_h)
    error_mid_h10 = error_calculation(traj_mid_h10, traj_rk4_h10)
    plot_error_two_steps(error_mid_h, error_mid_h10, h, "Midpoint vs RK4")

    error_vscd_h = error_calculation(traj_vscd_h, traj_rk4_h)
    error_vscd_h10 = error_calculation(traj_vscd_h10, traj_rk4_h10)
    plot_error_two_steps(error_vscd_h, error_vscd_h10, h, "VSCD vs RK4")


if __name__ == '__main__':
    main()