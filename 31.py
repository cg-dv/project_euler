#!/usr/bin/env python

denoms = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200
combinations = [1] + [0] * total
for coin in denoms:
    for i in range(coin, total + 1):
        combinations[i] += combinations[i - coin]
print(combinations[200])
