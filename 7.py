#!/usr/bin/env python

import sieve

def ans():
    primes = sieve.eratosthenes(1000000)
    return primes[10000]

print(ans())
