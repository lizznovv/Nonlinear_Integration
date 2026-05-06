import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_projections(trajectory, title="Trajectory"):

    traj = np.array(trajectory)

    x = traj[:, 0]
    y = traj[:, 1]
    z = traj[:, 2]

    plt.figure(figsize=(12, 4))

    # (x, y)
    plt.subplot(1, 3, 1)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("x-y")

    # (x, z)
    plt.subplot(1, 3, 2)
    plt.plot(x, z)
    plt.xlabel("x")
    plt.ylabel("z")
    plt.title("x-z")

    # (y, z)
    plt.subplot(1, 3, 3)
    plt.plot(y, z)
    plt.xlabel("y")
    plt.ylabel("z")
    plt.title("y-z")

    plt.suptitle(title)
    plt.tight_layout()
    plt.show()

def plot_3d(trajectory, title="3D Trajectory"):

    traj = np.array(trajectory)

    x = traj[:, 0]
    y = traj[:, 1]
    z = traj[:, 2]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x, y, z)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title)

    plt.show()