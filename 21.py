#!/usr/bin/env python
# Too slow
def divisor_sum(n):
    d_sum = 0
    for i in range(1, (n//2) + 1):
        if (n % i == 0):
            d_sum += i
    return d_sum

def are_amicable(n,m):
    if (n == divisor_sum(m) and (m == divisor_sum(n))):
        return True
    else:
        return False
total = 0
for i in range(1,10001):
    for j in range(1,10001):
        if are_amicable(i,j) and (i != j):
            total += j

print(total)
