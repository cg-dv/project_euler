#!/usr/bin/env python

def fib(n):
    if n < 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def ans():
    i = 1
    f = fib(i)
    sum = 0
    while f < 4000000:
        if f % 2 == 0:
            sum += f
        i += 1
        f = fib(i)
    return sum

print(ans())
