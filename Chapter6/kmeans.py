#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: kmeans.py
#    Created:       <2021/07/20 12:12:14>
#    Last Modified: <2021/07/20 12:16:07>

from __future__ import annotations
from typing import TypeVar, Generic, List, Sequence
from copy import deepcopy
from functools import partial
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass
from data_point import DataPoint

def zscores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)
    if std == 0: # 分散がなければ全てに対して 0 を返す
        return [0] * len(original)
    return [(x - avg) / std for x in original]
