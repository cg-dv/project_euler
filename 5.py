#!/usr/bin/env python

def all_divisors(n):
    all_divisors = False
    dividend = 5000 
    sum = 0
    while not all_divisors:
        for i in range(1,n+1):
            if (dividend % i == 0):
                sum += 1
        if sum == n:
            return dividend
        else:
            dividend += 2 
            sum = 0
    return dividend 

print(all_divisors(20))
