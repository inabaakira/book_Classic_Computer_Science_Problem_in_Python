#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: kmeans.py
#    Created:       <2021/07/20 12:12:14>
#    Last Modified: <2021/08/28 14:47:01>

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

    def __init__(self, k: int, points: List[Point]) -> None:
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

    def _dimension_slice(self, dimension: int) -> List[float]:
        return [x.dimensions[dimension] for x in self._points]

    def _zscore_normalize(self) -> None:
        zscored: List[List[float]] = [[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions):
            dimension_slice: List[float] = self._dimension_slice(dimension)
            for index, zscore in enumerate(zscores(dimension_slice)):
                zscored[index].append(zscore)
        for i in range(len(self._points)):
            self._points[i].dimensions = tuple(zscored[i])

    def _random_point(self) -> DataPoint:
        rand_dimensions: List[float] = []
        for dimension in range(self._points[0].num_dimensions):
            values: List[float] = self._dimension_slice(dimension)
            rand_value: float = uniform(min(values), max(values))
            rand_dimensions.append(rand_value)
        return DataPoint(rand_dimensions)

    # 各 point に最も近い cluster の centroid を発見し，
    # その point を該当の cluster に登録する．
    def _assign_clusters(self) -> None:
        for point in self._points:
            closest: DataPoint = min(self._centroids,
                                     key = partial(DataPoint.distance, point))
            idx: int = self._centroids.index(closest)
            cluster: KMeans.Cluster = self._clusters[idx]
            cluster.points.append(point)

    # 各 cluster の center を見つけ，centroid をそこに移動する．
    def _generate_centroid(self) -> None:
        for cluster in self._clusters:
            if len(cluster.points) == 0: # points が無ければ centroid はそのまま
                continue
            means: List[float] = []
            for dimension in range(cluster.points[0].num_dimensions):
                dimension_slice: List[float] = \
                    [p.dimensions[dimension] for p in cluster.points]
                means.append(mean(dimension_slice))
            cluster.centroid = DataPoint(means)

    def run(self, max_iterations: int = 100) -> List[KMeans.Cluster]:
        for iteration in range(max_iterations):
            # 全ての cluster をクリアする．
            for cluster in self._clusters:
                cluster.points.clear()
                # 各 point が最も近い cluster を見つけてそこに登録する．
                self._assign_clusters()
                old_centroids: List[DataPoint] = deepcopy(self._centroids) # 現在を保存する．
                self._generate_centroid() # 新しい centroids を見つける．
                if old_centroids == self._centroids: # centroids が変わらない場合
                    print(f"Converged after {iteration} iterations")
                    return self._clusters
            return self._clusters


if __name__ == "__main__":
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([3.0, 1.5, 2.5])
    kmeans_test: KMeans[DataPoint] = KMeans(2, [point1, point2, point3])
    test_clusters: List[KMeans.Cluster] = kmeans_test.run()
    for index, cluster in enumerate(test_clusters):
        print(f"Cluster {index}: {cluster.points}")
