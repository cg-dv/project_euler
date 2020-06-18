#!/usr/bin/env python

import itertools

def is_pandigital(n):
    return ''.join(sorted(list(str(n)))) == '123456789' 

def ans():
    pan_digitals = []

    s = ''
    for i in range(10000):
        s = ''
        for k in range(1,10):
            s = s + str(i * k)
            if is_pandigital(s):
                pan_digitals.append(s)

    return (max(pan_digitals))

print(ans())
