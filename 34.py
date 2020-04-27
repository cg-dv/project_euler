#!/usr/bin/env python

import math

def fac_sum(n):
    fac_sum = 0
    s = str(n)
    for char in s:
        fac_sum += math.factorial(int(char))
    if n == fac_sum:
        return n
    else:
        return 0 

def ans(n):
    total = 0
    for i in range(3,n):
        total += fac_sum(i)
    return total

print(ans(100000))
