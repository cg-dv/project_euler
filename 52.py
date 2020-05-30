#!/usr/bin/env python

n = 123456
while 1:
    if sorted(str(n)) == sorted(str(2 * n)) == sorted(str(3 * n)) == sorted(str(4 * n)) == sorted(str(5 * n)) == sorted(str(6 * n)):
        print(n)
    n += 1
