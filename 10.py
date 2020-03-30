#!/usr/bin/env python

import sieve

def ans():
    return sum(sieve.eratosthenes(2000000))

print(ans())
