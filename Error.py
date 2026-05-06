import numpy as np
from matplotlib import pyplot as plt


def error_calculation(trajectory1, trajectory2):
    error = []
    traj1 = np.array(trajectory1)
    traj2 = np.array(trajectory2)

    for i in range(len(traj1)):
        dx = traj1[i][0] - traj2[i][0]
        dy = traj1[i][1] - traj2[i][1]
        dz = traj1[i][2] - traj2[i][2]
        error.append(np.sqrt(dx**2 + dy**2 + dz**2))

    return error

def plot_error_two_steps(error_h, error_h10, h, title="Error comparison"):

    t1 = np.arange(len(error_h)) * h
    t2 = np.arange(len(error_h10)) * (h / 10)

    plt.figure()

    plt.plot(t1, error_h, label="h")
    plt.plot(t2, error_h10, label="h/10")

    plt.yscale('log')

    plt.xlabel("time")
    plt.ylabel("error")
    plt.title(title)

    plt.legend()
    plt.grid()

    plt.show()