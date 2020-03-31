#!/usr/bin/env python

# Number of distinct lattice paths from upper left-hand corner to lower right-
# hand corner in n x n matrix: 2n choose n

import math

def nCk(n, k):
    return (math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))

print(nCk(40,20))
