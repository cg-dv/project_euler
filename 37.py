#!/usr/bin/env python

import sieve

def l_trun(s):
    l = []
    for i, char in enumerate(s):
        l.append(s[i:])
    return l

def r_trun(s):
    l = []
    for i, char in enumerate(s):
        l.append(s[:i+1])
    return l

def l_and_r_primes(n):
    l_prime = (int(i) in primes for i in l_trun(str(n)))
    r_prime = (int(i) in primes for i in r_trun(str(n)))
    if all(l_prime) and all(r_prime):
        return True
    else:
        return False

primes = sieve.eratosthenes(1000000)

def ans():
    total = 0
    for prime in primes:
        if prime > 7 and l_and_r_primes(prime):
            total += prime
    return total

print(ans())
