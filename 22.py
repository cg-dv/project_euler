#!/usr/bin/env python

letters = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

n_lines = []
for line in open('22.txt'):
    n_lines.append(line)
names = n_lines[0].split(',')

def name_scores_total(names):
    names = [n.strip('\'\"') for n in names]
    names.sort()
    total = 0
    for i, name in enumerate(names):
        name_count = 0
        for char in name:
            name_count += letters[char]
        name_score = (i + 1) * name_count
        total += name_score
    return total

print(name_scores_total(names))
