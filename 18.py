#!/usr/bin/env python

n_lines = []
for line in open('18.txt'):
    line = line.rstrip('\n\r')
    n_lines.append(line)

nested_list = [map(int, line.split()) for line in n_lines]

def max_path(l):
    for i in range(len(l)-2, -1, -1):
        for j, item in enumerate(nested_list[i]):
            if (nested_list[i+1][j] > nested_list[i+1][j+1]):
                nested_list[i][j] = item + nested_list[i+1][j]
            else:
                nested_list[i][j] = item + nested_list[i+1][j+1]
    return nested_list[0][0]

print(max_path(nested_list))
