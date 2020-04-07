#!/usr/bin/env python

def fifth(n):
    return int(n) ** 5 

def ans():
    total = 0
    for i in range(1000000):
        if ((sum(map(fifth, list(str(i))))) == i):
            total += i
    return total - 1
print(ans())
