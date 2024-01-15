"""
different combinatorial mathmatics
"""

import numpy as np
import math
from scipy.special import binom as calbinom


def rand_distribution(N) -> float:
    """
    Random distribution

    Params:
    - N: number of inputs (ex. 52 cards in a deck of cards)

    return:
    float with how many distributions are possible

    """
    return math.factorial(N)


def stirling_app(N) -> float:
    """
    Stirling's approcimation for N!

    Params:
    - N: number of inputs (ex. 52 cards in a deck of cards)

    return:
    float with approximation of number of possible distributions

    """
    return N**N * np.exp(-N) * np.sqrt(2 * np.pi * N)


def stirling_app_ln(N) -> float:
    """
    Stirling's approximation for ln(N!)

    Params:
    - N: number of inputs (ex. 52 cards in a deck of cards)

    return:
    float with approximation of number of possible distributions

    """
    return N * np.log(N) - N


def two_state_microstates(N) -> float:
    """
    Number of microstates

    params:
    - N: how many times one thing is tested. 1 coin 20 times or 20 coins 1 time.

    return:
    float with microstates
    """
    return 2**N


def get_binom_info(n, N) -> dict:
    """
    creates Binomial object and then prints things of relevance

    params:
    - n: number of datapoints
    - N: total number of tries

    returns:
    probability of a microstate
    probability of a macrostate
    """
    probmacroout = calbinom(N, n)

    probmicroout = 1 / two_state_microstates(N)

    numofmicro = two_state_microstates(N)

    print(f"Probability of a macrostate: {probmacroout}")
    print(f"Probability of a microstate: {probmicroout}")
    print(f"Number of microstates: {numofmicro}")


