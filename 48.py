#!/usr/bin/env python

def self_power_sum(n):
    total = 0
    for i in range(1,n):
        total += i ** i 
    return total

print(self_power_sum(1001))
