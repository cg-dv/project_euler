#!/usr/bin/env python

def is_pandigital(n):
    return ''.join(sorted(list(str(n)))) == '123456789' 

def ans():
    d = {}
    total = 0
    for i in range(1,333):
        for j in range(1,2000):
            if is_pandigital(str(i) + str(j) + str(i*j)):
                d[i*j] = (str(i) + str(j) + str(i*j)) 
                print(str(i) + str(j) + str(i*j)) 
    for i in d:
        print(i,total)
        total += i
    print(d)
    return total 

print(ans())
