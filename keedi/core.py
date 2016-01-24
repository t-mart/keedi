from itertools import tee

import numpy as np


class KeediException(Exception):
    pass


class IncomputableRateException(KeediException):
    pass


def word_distance(word, keyboard):
    if len(word) == 1:
        return 0
    word_coords = (keyboard.coord_map[c] for c in word)
    return sum(distance(a, b) for a, b in pairwise(word_coords))


def word_distance_rate(word, keyboard, precomputation=None):
    if precomputation is None:
        precomputation = word_distance(word, keyboard)
    pairwise_count = len(word) - 1
    if pairwise_count == 0:
        raise IncomputableRateException("Cannot compute rate for word "
                                        "'%s' because it only has 1 "
                                        "character." % word)
    return precomputation / (len(word) - 1)


def distance(a, b):
    """source: http://stackoverflow.com/a/17936744/235992
    :param a: a numpy array of the first coordinate
    :param b: a numpy array of the second coordinate
    :return: the euclidean distance between these coordinates
    """
    distances = (a-b)**2
    distances = distances.sum(axis=-1)
    distances = np.sqrt(distances)
    return distances

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...
    source: https://docs.python.org/3/library/itertools.html"""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)