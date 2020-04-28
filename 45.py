#!/usr/bin/env python

def triangular(n):
    return n * (n + 1) / 2

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

def ans():
    for i in triangulars: 
        if (i in pentagonals) and (i in hexagonals):
            return i

triangulars = [triangular(i) for i in range(286,1000000)]
pentagonals = [pentagonal(i) for i in range(166,1000000)]
hexagonals = [hexagonal(i) for i in range(144,1000000)]

print(ans())
