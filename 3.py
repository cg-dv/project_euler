#!/usr/bin/env python

import math 
import sieve

def ans():
    max = 0
    sqrt = int(math.sqrt(600851475143))
    primes = sieve.eratosthenes(sqrt)
    for prime in primes: 
        if 600851475143 % prime == 0: 
            max = prime
    return max

print(ans())
