#!/usr/bin/env python

i_product = 1
j_product = 1
for i in range(11,100):
    for j in range(11,100):
        if j % 10 != 0 and j % 11 != 0 and str(i)[1] == str(j)[0]:
            if ((float(str(i)[0]) / float(str(j)[1])) == float(i) / j):
                i_product = i * i_product 
                j_product = j * j_product

print(float(j_product) / i_product)
