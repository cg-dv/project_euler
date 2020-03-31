#!/usr/bin/env python

n_lines = []
for line in open('11.txt'):
    line = line.rstrip('\n\r')
    n_lines.append(line)

sub_strings = []
for line in n_lines:
    sub_strings.append(line.split())

def horizontal():
    products = [] 
    for i, row in enumerate(sub_strings):
        for j in range(len(row)-3):
            products.append(int(sub_strings[i][j]) * int(sub_strings[i][j+1]) * int(sub_strings[i][j+2]) * int(sub_strings[i][j+3]))
    return products

def vertical():
    products = [] 
    for i in range(len(sub_strings)-3):
        for j in range(len(sub_strings)):
            products.append(int(sub_strings[i][j]) * int(sub_strings[i+1][j]) * int(sub_strings[i+2][j]) * int(sub_strings[i+3][j]))
    return products

def diagonal_lr():
    products = [] 
    for i in range(len(sub_strings)-3):
        for j in range(len(sub_strings)-3):
            products.append(int(sub_strings[i][j]) * int(sub_strings[i+1][j+1]) * int(sub_strings[i+2][j+2]) * int(sub_strings[i+3][j+3]))
    return products

def diagonal_rl():
    products = [] 
    for i in range(len(sub_strings)-3):
        for j in range(len(sub_strings)-3):
            products.append(int(sub_strings[i+3][j]) * int(sub_strings[i+2][j+1]) * int(sub_strings[i+1][j+2]) * int(sub_strings[i][j+3]))
    return products

def ans():
    nested_product_list = []
    nested_product_list.append(horizontal())
    nested_product_list.append(vertical())
    nested_product_list.append(diagonal_lr())
    nested_product_list.append(diagonal_rl())

    all_products = [item for l in nested_product_list for item in l]
    return max(all_products)

print(ans())
