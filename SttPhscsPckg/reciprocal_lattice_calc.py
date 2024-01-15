# -*- coding: utf-8 -*-

"""
rather bad attempts at calculating reciprocal lattice vectors
"""

import numpy as np


def calc_rec_lat(a1=[1, 1], a2=[1, 1], a3=""):
    """
    Calculate the reciprocal lattice of a crystal structure.
    in N-dimensions length of list = N
    Parameters:
    a1 (list): A list of floats representing the first lattice vector.
    a2 (list): A list of floats representing the second lattice vector.
    a3 (list, optional): A list of floats representing the third lattice
    vector. Defaults to "".

    Returns:
    tuple: A tuple of 3 lists representing the reciprocal lattice vectors.
    """
    if a3:
        real = np.array([a1, a2, a3])
        cross23 = np.cross(real[1], real[2])
        cross13 = np.cross(real[0], real[2])
        cross12 = np.cross(real[0], real[1])
        b1 = 2 * np.pi * cross23 / np.dot(real[0], cross23)
        b2 = 2 * np.pi * cross13 / np.dot(real[1], cross13)
        b3 = 2 * np.pi * cross12 / np.dot(real[2], cross12)

        return b1, b2, b3
    else:
        real = np.array([a1, a2])
        Q = np.array([[0, -1], [1, 0]])

        b1 = 2 * np.pi * np.dot(Q, real[1]) / (np.dot(real[0], np.dot(Q, real[1])))
        b2 = 2 * np.pi * np.dot(Q, real[0]) / (np.dot(real[1], np.dot(Q, real[0])))

        return b1, b2
