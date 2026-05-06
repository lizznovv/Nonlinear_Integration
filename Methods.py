import numpy as np
from System import Rossler_attractor

def euler(state, coefs, h):

    derivatives = Rossler_attractor(state[0], state[1], state[2], coefs)

    x = state[0] + h * derivatives[0]
    y = state[1] + h * derivatives[1]
    z = state[2] + h * derivatives[2]

    return x, y, z

def e_cromer(state, coefs, h):

    derivatives = Rossler_attractor(state[0], state[1], state[2], coefs)
    x = state[0] + h * derivatives[0]

    derivatives = Rossler_attractor(x, state[1], state[2], coefs)
    y = state[1] + h * derivatives[1]

    derivatives = Rossler_attractor(x, y, state[2], coefs)
    z = state[2] + h * derivatives[2]

    return x, y, z

def midpoint(state, coefs, h):

    derivatives = Rossler_attractor(state[0], state[1], state[2], coefs)

    half_x = state[0] + (h/2) * derivatives[0]
    half_y = state[1] + (h/2) * derivatives[1]
    half_z = state[2] + (h/2) * derivatives[2]

    derivatives = Rossler_attractor(half_x, half_y, half_z, coefs)

    x = state[0] + h * derivatives[0]
    y = state[1] + h * derivatives[1]
    z = state[2] + h * derivatives[2]

    return x, y, z

def vscd(state, coefs, h, s = 0.5):

    h1 = s * h
    h2 = (1 - s) * h

    derivatives = Rossler_attractor(state[0], state[1], state[2], coefs)
    half_x = state[0] + h1 * derivatives[0]

    derivatives = Rossler_attractor(half_x, state[1], state[2], coefs)
    half_y = state[1] + h1 * derivatives[1]

    derivatives = Rossler_attractor(half_x, half_y, state[2], coefs)
    half_z = state[2] + h1 * derivatives[2]

    z = (half_z + h2 * coefs[1]) / (1 - h2 * half_x + h2 * coefs[2])
    y = (half_y + h2 * half_x) / (1 - h2 * coefs[0])
    x = half_x - h2 * y - h2 * z

    return x, y, z

def rk4(state, coefs, h):

    derivatives = Rossler_attractor(state[0], state[1], state[2], coefs)
    k1X = derivatives[0]
    k1Y = derivatives[1]
    k1Z = derivatives[2]

    derivatives = Rossler_attractor(state[0] + k1X * (h/2), state[1]+ k1Y * (h/2), state[2]+ k1Z * (h/2), coefs)
    k2X = derivatives[0]
    k2Y = derivatives[1]
    k2Z = derivatives[2]

    derivatives = Rossler_attractor(state[0] + k2X * (h/2), state[1]+ k2Y * (h/2), state[2]+ k2Z * (h/2), coefs)
    k3X = derivatives[0]
    k3Y = derivatives[1]
    k3Z = derivatives[2]

    derivatives = Rossler_attractor(state[0] + k3X * h, state[1]+ k3Y * h, state[2]+ k3Z * h, coefs)
    k4X = derivatives[0]
    k4Y = derivatives[1]
    k4Z = derivatives[2]

    x = state[0] + (h/6) * (k1X + 2 * k2X + 2 * k3X + k4X)
    y = state[1] + (h/6) * (k1Y + 2 * k2Y + 2 * k3Y + k4Y)
    z = state[2] + (h/6) * (k1Z + 2 * k2Z + 2 * k3Z + k4Z)

    return x, y, z