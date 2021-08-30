#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: governors.py
#    Created:       <2021/08/30 11:25:14>
#    Last Modified: <2021/08/30 11:29:15>

from __future__ import annotations
from typing import List
from data_point import DataPoint
from kmeans import KMeans

class Governor(DataPoint):
    def __init__(self, longitude: float, age: float, state: str) -> None:
        super().__init__([longitude, age])
        self.longitude = longitude
        self.age = age
        self.state = state

    def __repr__(self) -> str:
        return f"{self.state}: (longitude: {self.longitude}, age: {self.age})"
