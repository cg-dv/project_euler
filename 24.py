#!/usr/bin/env python

import math
import itertools

s = '0123456789'

p = itertools.permutations(s)

for i, elem in enumerate(p):
    if i == (1000000 - 1):
        print(''.join(elem))
