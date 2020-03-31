#!/usr/bin/env python

def collatz(n, m):
    if n == 1:
        return m + 1 
    if (n % 2 == 0):
        return collatz(n // 2, m + 1)
    else:
        return collatz((3 * n) + 1, m + 1)

def ans():
    max_key = 1 
    max_value = 0
    for i in range(1,1000000):
        collatz_val = collatz(i,0)
        if collatz_val > max_value:
            max_value = collatz_val
            max_key = i
    return max_key

print(ans())
