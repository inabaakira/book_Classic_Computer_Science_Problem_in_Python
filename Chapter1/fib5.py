#!/usr/bin/python --
#-*- mode: python; coding: utf-8 -*-
# file: fib5.py
#    Created:       <2019/05/31 12:22:25>
#    Last Modified: <2019/05/31 12:26:07>

def fib5(n: int) -> int:
    if n == 0: return n # special case
    last: int = 0 # initially set fib(0)
    next: int = 1 # initially set fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    print(fib5(5))
    print(fib5(50))
