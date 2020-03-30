#!/usr/bin/env python

n_lines = []
for line in open('8.txt'):
    line = line.rstrip('\n\r')
    n_lines.append(line)

n_str = "".join(n_lines)
sub_strings = []
for i in range(len(n_str)-12):
    sub_strings.append(n_str[i:i+13])

def product(s):
    product = 1
    for i in s:
        product = product * int(i)
    return product

def max_product(l):
    products = []
    for sub_string in l:
        products.append(product(sub_string))
    return max(products)

def ans():
    return max_product(sub_strings)

print(ans())
