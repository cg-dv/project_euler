#!/usr/bin/env python

def ans():
    powers = []
    for i in range(100):
        powers.append([j ** i for j in range(1,1000)])

    count = 0
    for i, l in enumerate(powers):
        for j in l:
            if len(str(j)) == i:
                print(i, j)
                count += 1
    return count
print(ans())
