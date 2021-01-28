#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: weighted_edge.py
#    Created:       <2021/01/28 22:45:47>
#    Last Modified: <2021/01/28 22:50:21>

from __future__ import annotations
from dataclasses import dataclass
from edge import Edge

@dataclass
class WeightedEdge(Edge):
    weight: float

    def reversed(self) -> WeightedEdge:
        return WeightedEdge(self.v, self.u, self.weight)

    # edge を weight に従って順序付けし、
    # 最小の weight を持つ edge を見つけることができるようにする。
    def __lt__(self, other: WeightedEdge) -> bool:
        return self.weight < other.weight

    def __str__(self) -> str:
        return f"{self.u} {self.weight}> {self.v}"
