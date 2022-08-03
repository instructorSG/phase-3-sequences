#!/usr/bin/env python3
fib=[0,1]


def print_fibonacci(length):
    if length==0:
        print([])
    elif length==1:
        print([0])
    elif length==2:
        print([0,1])
    else:

        for x in range (2 ,length):
            a = fib[x-1]+fib[x-2]
            fib.append(a)
        print(fib)
