#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: graph.py
#    Created:       <2021/01/10 11:23:20>
#    Last Modified: <2021/01/10 11:25:44>

from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]
