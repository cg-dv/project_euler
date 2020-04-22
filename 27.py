#!/usr/bin/env python

import sieve

primes = sieve.eratosthenes(10000)

maximum = 0
max_i = 0 
max_j = 0 
for i in range(-1000,1000):
    for j in range(-1001,1001):
        k = 0
        while ((k ** 2) + (i * k) + j) in primes:
            k += 1
            if k > maximum:
                maximum = k
                max_i = i 
                max_j = j

print(max_i * max_j)
