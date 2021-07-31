#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: kmeans.py
#    Created:       <2021/07/20 12:12:14>
#    Last Modified: <2021/07/31 23:14:50>

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

Point = TypeVar('Point', bound=DataPoint)

class KMeans(Generic[Point]):
    @dataclass
    class Cluster:
        points: List[Point]
        centroid: DataPoint

    def __init__(self, k: int, point: List[Point]) -> None:
        if k < 1: # 負またはゼロ個の cluster に対して k-means は考えられない
            raise ValueError("k must be >= 1")
        self._points: List[Point] = points
        self._zscore_normalize()
        # ランダムな centroids で空の cluster を初期化する
        self._clusters: List[KMeans.Cluster] = []
        for _ in range(k):
            rand_point: DataPoint = self._random_point()
            cluster: KMeans.Cluster = KMeans.Cluster([], rand_point)
            self._clusters.append(cluster)

    @property
    def _centroids(self) -> List[DataPoint]:
        return [x.centroid for x in self._clusters]
