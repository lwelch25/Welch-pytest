#!/usr/bin/python3


def evens(n):
    '''
    Returns an list of even numbers from 0 to n inclusive.
    '''
    xs = range(n + 1)
    xs = filter(lambda x: x % 2 == 0, xs)
    return list(xs)
