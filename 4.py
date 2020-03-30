#!/usr/bin/env python

def ans():
    palindromes = []
    for i in range(900,1000):
        for j in range(900,1000):
            s = str(i * j)
            if (s == s[::-1]):
                palindromes.append(i * j)
    return max(palindromes)

print(ans())
