#!/usr/bin/env python

import sieve

def is_goldbach(n):
    for prime in primes:
        for square in squares:
            if n == (prime + (2 * square)):
                return True
    return False

odds = set([(2 * i + 1) for i in range(100000)])
primes = set(sieve.eratosthenes(100000))
squares = set([i ** 2 for i in range(1,1000)])

for i in range(2,100000):
    if i in odds and i not in primes:
        print(i)
        if not is_goldbach(i):
            print(i, 'Not Goldbach')
