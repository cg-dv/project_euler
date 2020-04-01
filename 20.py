#!/usr/bin/env python

import math

def ans():
    return sum(map(int, list(str(math.factorial(100)))))

print(ans())
