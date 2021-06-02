#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: dijkstra.py
#    Created:       <2021/02/04 22:28:03>
#    Last Modified: <2021/06/02 09:42:46>

from __future__ import annotations
from typing import TypeVar, List, Optional, Tuple, Dict
from dataclasses import dataclass
from mst import WeightedPath, print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V') # graph 内の vertex の型

@dataclass
class DijkstraNode:
    vertex: int
    distance: float

    def __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool:
        return self.distance == other.distance

def dijkstra(wg: WeightedGraph[V], root: V) \
    -> Tuple[List[Optional[float]], Dict[int, WeightedEdge]]:

    first: int = wg.index_of(root) # 出発点の index を見つける
    # 最初は距離は分からない
    distances: List[Optional[float]] = [None] * wg.vertex_count
    distances[first] = 0
    path_dict: Dict[int, WeightedEdge] = {} # 各 vertex への行き方
    pq: PriorityQueue[DijkstraNode] = PriorityQueue()
    pq.push(DijkstraNode(first, 0))

    while not pq.empty:
        u: int = pq.pop().vertex # 次に近い vertex へ
        dist_u: float = distances[u]
        for we in wg.edges_for_index(u):
            # この vertex への古い距離
            dist_v: float = distances[we.v]
            # 古い距離が無い、またはより短い path が見つかった場合
            if dist_v is None or dist_v > we.weight + dist_u:
                # この vertex への距離を更新
                distances[we.v] = we.weight + dist_u
                # この vertex への最短の path の edge を更新
                path_dict[we.v] = we
                # 探索する
                pq.push(DijkstraNode(we.v, we.weight + dist_u))

    return distances, path_dict

# dijkstra の結果に簡単にアクセスするための helper function
def distance_array_to_vertex_dict(
        wg: WeightedGraph[V],
        distances: List[Optional[float]]) -> Dict[V, Optional[float]]:
    distance_dict: Dict[V, Optional[float]] = {}
    for i in range(len(distances)):
        distance_dict[wg.vertex_at(i)] = distances[i]
    return distance_dict

# 各 node へ至る edge の dictionary を取り、start から end に至る edge の list を返す
def path_dict_to_path(start: int,
                      end: int,
                      path_dict: Dict[int, WeightedEdge]) -> WeightedEdge:
    if len(path_dict) == 0:
        return []
    edge_path: WeightedPath = []
    e: WeightedEdge = path_dict[end]
    edge_path.append(e)
    while e.u != start:
        e = path_dict[e.u]
        edge_path.append(e)
    return list(reversed(edge_path))
