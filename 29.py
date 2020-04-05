#!/usr/bin/env python

def distinct_powers():
    results = []
    for i in range(2,101):
        for j in range(2,101):
            results.append(i ** j)
            results.append(j ** i)
    return len(set(results))

print(distinct_powers())
