#!/usr/bin/env python
def ans(n):
    i = 1
    k = 2
    count = -1 
    total = 1 
    while i < (n ** 2):
        count += 1
        if count >= 4:
            k += 2
            count = 0
        i += k
        total += i
    return total

print(ans(1001))
