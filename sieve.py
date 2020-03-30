#!/usr/bin/env python

import math

# Implementation of the Sieve of Eratosthenes - takes n as input, returns list
# of all primes less than n

def eratosthenes(n):
    primes = [True] * n
    for i in range(2,int(math.sqrt(n))):
        if primes[i]:
            for j in range(n-1):
                k = ((i ** 2) + (i * j))
                if k < n:
                    primes[k] = False
    
    primes_list = []
    for i, prime in enumerate(primes):
        if prime:
            primes_list.append(i)
    return primes_list[2:]
