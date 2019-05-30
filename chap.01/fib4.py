#!/usr/bin/python --
#-*- mode: python; coding: utf-8 -*-
# file: fib4.py
#    Created:       <2019/05/31 11:22:14>
#    Last Modified: <2019/05/31 11:26:27>

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int: # same difinition as fib2()
    if n < 2: # base case
        return n
    return fib4(n - 2) + fib4(n - 1) # recursive case

if __name__ == "__main__":
    print(fib4(5))
    print(fib4(50))
