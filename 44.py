#!/usr/bin/env python

def pentagonal(n):
    return n * (3 * n - 1) / 2

def sum_dif_pent(m,n):
    return ((m in pentagonals) and (n in pentagonals) and ((m - n) in pentagonals) and (m + n) in pentagonals)

def ans():

    results = []
    for i in pentagonals:
        for j in pentagonals:
            if sum_dif_pent(i,j):
                results.append(j - i)

    return abs(min(results))

pentagonals = set([pentagonal(i) for i in range(1000,10000)])

print(ans())
