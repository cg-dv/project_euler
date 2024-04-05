#!/usr/bin/env python

import decimal

def frac_dec(n):
    return decimal.Decimal(1) / decimal.Decimal(n)

for i in range(1, 100):
    print(decimal.Decimal(i), frac_dec(decimal.Decimal(i)))
