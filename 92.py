#!/usr/bin/env python

def sq_chain(n):
    if n == 89 or n == 1:
        return n
    else:
        sum = 0
        
        for char in str(n):
            sum += (int(char) ** 2)

        return sq_chain(sum)
def ans():
    count = 0
    for i in range(1,10000000):
        if sq_chain(i) == 89:
            count += 1
    return count

print(ans())
