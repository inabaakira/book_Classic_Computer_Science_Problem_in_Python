#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: util.py
#    Created:       <2021/10/28 14:21:30>
#    Last Modified: <2021/10/28 14:23:03>

from typing import list
from math import exp

# 2つのベクトルのドット積
def dot_product(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))
