#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: mst.py
#    Created:       <2021/01/23 23:38:42>
#    Last Modified: <2021/01/23 23:41:53>

from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V')
WeightedPath = List[WeightedEdge]

def tptal_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])
