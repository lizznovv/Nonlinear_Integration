import numpy as np

def Rossler_attractor(x, y, z, coefs):
    dx = -y - z
    dy = x + coefs[0] * y
    dz = coefs[1] + z * (x - coefs[2])

    return dx, dy, dz
