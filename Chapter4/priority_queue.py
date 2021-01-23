#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: priority_queue.py
#    Created:       <2021/01/20 17:37:57>
#    Last Modified: <2021/01/23 15:17:59>

from typing import TypeVar, Generic, List
from heapq import heappush, heappop

T = TypeVar('T')

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        heappush(self._container, item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)
