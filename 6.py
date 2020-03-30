#!/usr/bin/env python

def sum_of_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i ** 2
    return sum

def square_of_sum(n):
    return (sum(i for i in range(1,n+1)) ** 2)

def diff_sum_squares_square_sums(n):
    return square_of_sum(n) - sum_of_squares(n)

print(diff_sum_squares_square_sums(100))
