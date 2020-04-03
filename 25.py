#!/usr/bin/env python

#!/usr/bin/env python

def ans():
    i = 0
    for i in range(2,100000):
        fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
        if len(str(fib_dict[i])) == 1000:
            return i+1

fib_dict = {0:1,1:1}
print(ans())
