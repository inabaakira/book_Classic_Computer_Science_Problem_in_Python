#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: util.py
#    Created:       <2021/10/28 14:21:30>
#    Last Modified: <2021/10/29 10:01:22>

from typing import list
from math import exp

# 2つのベクトルのドット積
def dot_product(xs: List[float], ys: List[float]) -> float:
    return sum(x * y for x, y in zip(xs, ys))

# the classic sigmoid activation function
def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + exp(-x))

def derivative_sigmoid(x: float) -> float:
    sig: float = sigmoid(x)
    return sig * (1 - sig)
