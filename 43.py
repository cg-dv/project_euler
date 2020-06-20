#!/usr/bin/env python

import itertools

def is_pandigital(n):
    return ''.join(sorted(list(str(n)))) == '1234567890' 

def divis(n):
    count = 0
    for i, char in enumerate(str(n)):
        if 0 < i < len(str(n)) - 2:
            if int(str(n)[i:i+3]) % divisors[i-1] == 0:
                count += 1
        if count == len(divisors):
            return True
    return False

p = itertools.permutations('1234567890')
divisors = [2,3,5,7,11,13,17]

total = 0
for perm in p:
    if divis((int(''.join(perm)))):
        total += int(''.join(perm))

print(total)
