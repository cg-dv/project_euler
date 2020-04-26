#!/usr/bin/env python

letters = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

n_lines = []
for line in open('42.txt'):
    # n_lines.append(line)
    n_lines.append(line.strip('\"'))
words = n_lines[0].split(',')

def tri(n):
    return (n * (n + 1)) // 2

tri_set = set([tri(i) for i in range(1000)]) 

tri_count = 0 
max_word_val = 0
for word in words:
    word = word.strip('\"')
    word_sum = sum((letters[char] for char in word))
    if word_sum in tri_set:
        tri_count += 1

print(tri_count)
