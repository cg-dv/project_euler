#!/usr/bin/env python

def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False

def is_reversible(n):
    total = n + int(str(n)[::-1])
    if str(n)[-1] == str(0):
        return False
    count = 0
    for char in str(total):
        if is_odd(int(char)):
            count += 1
    if count == len(str(total)):
        return True
    else:
        return False

def ans():
    n_count = 0
    for i in range(1,10 ** 9):
        if is_reversible(i):
            n_count += 1
    return n_count

print(ans())
