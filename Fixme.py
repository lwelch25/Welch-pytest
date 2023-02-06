#!/usr/bin/python3


def evens(n):
    return list(filter(lambda x: x % 2 == 0, map(lambda x: x, range(0, n+1))))
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
