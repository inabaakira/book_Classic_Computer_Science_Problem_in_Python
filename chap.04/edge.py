#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: edge.py
#    Created:       <2021/01/07 12:13:13>
#    Last Modified: <2021/01/07 12:15:19>

from __future__ import annotations
from dataclasses import dataclasses

@dataclass
class Edge:
    u: int
    v: int

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"
