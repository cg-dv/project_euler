#!/usr/bin/env python

def digit_sum(n):
    return sum(int(char) for char in str(n))

def ans():
    max_sum = 0
    for i in range(1,101):
        for j in range(1,101):
            d_sum = digit_sum(i ** j)
            if digit_sum(i ** j) > max_sum:
                max_sum = d_sum
    return max_sum

print(ans())
