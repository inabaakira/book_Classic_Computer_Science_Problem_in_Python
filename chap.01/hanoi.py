#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: hanoi.py
#    Created:       <2019/07/28 20:07:50>
#    Last Modified: <2019/07/28 20:10:19>

from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)
