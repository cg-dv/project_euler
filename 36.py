#!/usr/bin/env python

def is_palindrome(s):
    return s == s[::-1]

count = 0
for i in range(1000000):
    if is_palindrome(str(i)) and is_palindrome(str(bin(i)[2:])):
        count += i

print(count)
