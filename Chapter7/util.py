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

# assume all rows are of equal length
# and feature scale each column to be in the range 0 - 1
def normalize_by_feature_scaling(dataset: List[List[float]]) -> None:
    for col_num in range(len(dataset[0])):
        column: List[float] = [row[col_num] for row in datase]
        maximum = max(column)
        minimum = min(column)
        for row_num in range(len(dataset)):
            dataset[row_num][col_num] = \
                (dataset[row_num][col_num] - minumum) / (maximum - minimum)
