#!/usr/bin/env python

n_lines = []
for line in open('59.txt'):
    n_lines.append(line.split(',')) 

words = []
for line in open('words.txt'):
    words.append(line.strip('\n'))
words = set(words)

common = ['the', 'of', 'to', 'and', 'you', 'that', 'he', 'was']

n_list = []
for line in n_lines:
    for n in line:
        n_list.append(int(n))

s = ''
keys = [] 
for i in range(97,123):
    for j in range(97, 123):
        for k in range(97,123):
            keys.append(chr(i) + chr(j) + chr(k))

# i = -1 
# for key in keys:
# message = ''
# for n in n_list:
    # i += 1
    # if i % 3 == 0:
        # i = 0
    # message = message + (chr(ord('exp'[i]) ^ n))
    # if 'the' in message and 'and' in message:
    # print(key, '\n' * 3)
    # print(message)

def ans():
    i = -1 
    message = ''
    for n in n_list:
        i += 1
        if i % 3 == 0:
            i = 0
        message = message + (chr(ord('exp'[i]) ^ n))
        total = 0
        for char in message:
            total += ord(char)
    return total

print(ans())
