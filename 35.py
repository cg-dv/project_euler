#!/usr/bin/env python

import itertools
import sieve

n = 1000000
primes = set(sieve.eratosthenes(n))
cir_primes = []

def rotations(s):
    l = []
    for i, char in enumerate(s):
        l.append(s[i:] + s[:i])
    return l

def ans():
    for i in primes: 
        l = rotations(str(i))
        is_cir = [int(i) in primes for i in l]
        if all(is_cir):
            cir_primes.append(i)
    return len(cir_primes)

print(ans())
