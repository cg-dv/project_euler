#!/usr/bin/env python

def divisors(n):
    divisors = [] 
    for i in range(1,(n//2)+1):
        if (n % i == 0):
            divisors.append(i) 
    return set(divisors)

def d_sum(n):
    divisor_sum = 0 
    for i in range(1,(n//2)+1):
        if (n % i == 0):
            divisor_sum += i 
    return divisor_sum

def is_abundant(n):
    if (d_sum(n) > n):
        return True
    else:
        return False

def abundant_numbers(n):
    abundant_numbers = []
    for i in range(n):
        if is_abundant(i):
            abundant_numbers.append(i)
    return abundant_numbers

def abundant_summands(n, abundant_numbers):
    for i in range(1,(n//2) + 1):
        if (i in set(abundant_numbers)) and (n-i) in set(abundant_numbers): 
            return True 
    return False

def ans(abundant_numbers):
    total = 0
    for i in range(1,28124):
        print(i)
        if not abundant_summands(i, abundant_numbers):
            total += i
    return total

abundant_numbers = abundant_numbers(28124) 

print(ans(abundant_numbers))
