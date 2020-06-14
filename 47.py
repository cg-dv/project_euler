#!/usr/bin/env python

import sieve, math

def four_factors(n):
    factors = []
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
        if len(factors) == 4:
            return True
    return False

primes = sieve.eratosthenes(10000)

for i in range(10000000):
    if four_factors(i) and four_factors(i + 1) and four_factors(i + 2) and four_factors(i + 3):
        print(i)
