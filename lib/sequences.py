#!/usr/bin/env python3


def print_fibonacci(length):
    a,b = 0,1

    if length == 0:
        print([])
    elif length == 1:
        print([a])
    elif length == 2:
        print([a,b])
    else:
        fib = [a,b]
        for i in range(2,length):
            fib.append(fib[i-1]+fib[i-2])
        print(fib)

