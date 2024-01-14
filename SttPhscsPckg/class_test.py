"""
Used for testing
"""

import numpy as np

def test(n):
    """
    generates a test

    parameters:
        n: this is used as a number

    returns:
        a list of random number generated from one number
    """
    return np.linspace(n,n+1)


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]



mylist = [1,2,3,2,1,3]

print(len(mylist))

mylist.insert(1,8)

print(len(mylist))
