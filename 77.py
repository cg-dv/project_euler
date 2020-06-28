#!/usr/bin/env python

import sieve

for n in range(100):
    total = n 
    part = [1] + [0] * total 
    denom = sieve.eratosthenes(100) 

    for d in denom:
        for i in range(d, total + 1):
            part[i] += part[i - d]
    print(n, part[total])
