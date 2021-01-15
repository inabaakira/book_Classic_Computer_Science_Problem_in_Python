#!/usr/bin/python --
#-*- mode: python; coding: utf-8 -*-
# file: fib6.py
#    Created:       <2019/05/31 15:49:14>
#    Last Modified: <2019/05/31 15:57:34>

from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 # special case
    last: int = 0 # initially set fib6(0)
    next: int = 1 # initially set fib6(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step

if __name__ == "__main__":
    for i in fib6(50):
        print(i)
