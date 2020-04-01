#!/usr/bin/env python

import math

def tri_num(n):
    return (n * (n + 1)) // 2

def num_divisors(n):
    num_divisors = 0
    for i in range(1,(n//2)+1):
        if (n % i == 0):
            num_divisors += 1
    return num_divisors + 1

def ans():
    n = 8000
    while num_divisors(tri_num(n)) < 501:
        print(n, tri_num(n), num_divisors(tri_num(n)))
        n += 1
    return tri_num(n) 

print(ans())
