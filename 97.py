#!/usr/bin/env python

def ans():
    n = str(28433 * (2 ** 7830457) + 1) 
    return n[len(n)-10:]

print(ans())
