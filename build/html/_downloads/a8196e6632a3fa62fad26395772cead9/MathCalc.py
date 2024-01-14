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


def two_einstein(units_of_e, oscillators):
    """
    Important stuff about two einstein solids that are identical

    params:
    - units_of_e: units of energy shared between the two systems
    - oscillators: total number of oscillators in total system

    return:
    - number of macrostates
    - number of microstates
    - probability of finding all energy in one solid
    - probability of finding half energy in one solid
    """
    numofmacro = units_of_e + 1  # +1 because one solid can be empty giving a state with 0 energy

    numofmicro = calbinom(units_of_e + oscillators - 1, units_of_e)

    findallinoneprob = (
        calbinom(units_of_e + oscillators / 2 - 1, units_of_e) * calbinom(oscillators / 2 - 1, 0) / numofmicro
    )

    findhalfinonerob = calbinom(units_of_e / 2 + oscillators / 2 - 1, units_of_e / 2) ** 2 / numofmicro

    return "number of macrostates:{:e} \n microstates: {:e} \n probability of one solid with no energy: {:.5e} \n half the energy: {:.5e}".format(
        numofmacro, numofmicro, findallinoneprob, findhalfinonerob
    )
