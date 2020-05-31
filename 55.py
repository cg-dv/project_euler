#!/usr/bin/env python

def n_reverse_sum(n):
    return n + int(''.join(reversed(str(n))))

def is_palindrome(n):
    if str(n) == ''.join(reversed(str(n))):
        return True
    else:
        return False

def is_lychrel(n,i):
    if i == 50:
        return True

    count = i 
    k = n_reverse_sum(n)
    if is_palindrome(n_reverse_sum(n)):
        return False
    else:
        count += 1
        return is_lychrel(k, count)

def ans():
    count = 0
    for i in range(1,10001):
        if is_lychrel(i,0):
            count += 1
    return count

print(ans())
