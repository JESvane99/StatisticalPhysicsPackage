"""
Entropy calculations
"""
import numpy as np


from scipy.constants import Boltzmann as k_bm


def ES_entropy(N, q) -> float:
    S = N * k_bm * (np.log(q / N) + 1)

    return S


def ES_entropy_two(N):
    """
    calculating the entropy of a system of two identical
    Einstein solids whith approximation for large number of oscillators

    params:
    - N: number of oscillators for solid

    returns:
    - total entropy of the system as is, and in terms of k

    """

    S_tot = (4 * N * np.log(2) - 1 / 2 * np.log(8 * np.pi * N)) * k_bm

    S_tot_bm = S_tot / k_bm

    print(f"total entropy of the system: {S_tot}", "\n", f"Entropy in terms of Boltzmanns constant: {S_tot_bm}")


def ES_energy_qNlim(N, eps=1, T=298):
    """
    Calculating the energy of an Einstein solid in the limit of $q \ll N$
    taken from AnswersC.pdf problem 3.5

    params:
    - N: number of oscillators
    - eps: $\epsilon$ is the size of an energy unit. set to 1 just in cas
    - T: temperature in Kelvin
    """
    return N * eps * np.exp(-eps / (k_bm * T))


def ES_C_V_qNlim(N, T=298, eps=1):
    """Calculating the heat capacity of an Einstein solid in the limit of $q \ll N$
    taken from AnswersC.pdf problem 3.8

    params:
    params:
    - N: number of oscillators
    - eps: $\epsilon$ is the size of an energy unit. set to 1 just in cas
    - T: temperature in Kelvin

    return:
    heat capacity at constant volume in the limit of $q \ll N$

    """
    pass
