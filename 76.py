#!/usr/bin/env python

total = 100
part = [1] + [0] * 100
denom = [i for i in range(1,100)]

for d in denom:
    for i in range(d, total + 1):
        part[i] += part[i - d]
print(part[100])
