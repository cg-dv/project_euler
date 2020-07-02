#!/usr/bin/env python

max_n_solutions = 0

def is_right(a,b,c):
    if (a ** 2 + b ** 2) == (c ** 2):
        return True
    else:
        return False

def perim_check(a,b,c,p):
    if (a + b + c) == p:
        return True
    else:
        return False

d = {}
for i in range(1000):
    for j in range(1000):
        for k in range(1000):
            if (i ** 2 + j ** 2 == k ** 2) or (j ** 2 + k ** 2 == i ** 2) or (i ** 2 + k ** 2 == j ** 2):
                if sum([i,j,k]) <= 1000: 
                    if sum([i,j,k]) not in d:
                        d[sum([i,j,k])] = 1
                    else:
                        d[sum([i,j,k])] += 1
                        if d[sum([i,j,k])] > 7: 
                            print(i,j,k) 
                            print(sum([i,j,k])) 
max_sum = 0
for elem in d:
    if d[elem] > max_sum:
        max_sum = d[elem]
        print(elem, d[elem], max_sum)
print(max_sum)
