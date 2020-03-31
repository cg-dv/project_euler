#!/usr/bin/env python

n_lines = []
for line in open('13.txt'):
    line = line.rstrip('\n\r')
    n_lines.append(int(line))

print(str(sum(n_lines))[0:10])
