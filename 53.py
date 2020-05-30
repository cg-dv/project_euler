#!/usr/bin/env python

import math

def nCk(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def ans():
    count = 0
    for i in range(1,101):
        for j in range(1,i):
            if nCk(i,j) > 1000000:
                count += 1
    return count

print(ans())
