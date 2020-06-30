#!/usr/bin/env python

n_lines = []
for line in open('79.txt'):
    n_lines.append(line)
logins = [line.strip('\n') for line in n_lines]

order = []
for i, line in enumerate(logins):
    for char in line:
        if char not in order:
            order.append(char)

for n in sorted(logins):
    print(n)

# sorted elements manually
