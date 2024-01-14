"""
Calculations involving ideal gasses
"""


import scipy.constants as const

Room_T = 298  # K


def volume_id_gas(N):
    """
    Volume for N molecules for ideal gas
    at room temperature,
    and atmospheric pressure

    Math behind the scenes:

    P * V = N * k * T

    N -> number of mulecules
    P -> pressure
    V -> volume
    T -> temperature in Kelvin
    k -> boltzmanns constant

    params:
    -  N

    return:
    volume for N molecules as float m^3
    """
    return N * const.k * Room_T / const.atm


if __name__ == "__main__":
    print("hello world")
