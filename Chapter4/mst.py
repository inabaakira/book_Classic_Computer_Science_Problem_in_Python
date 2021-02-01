#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: mst.py
#    Created:       <2021/01/23 23:38:42>
#    Last Modified: <2021/01/31 00:11:10>

from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V')
WeightedPath = List[WeightedEdge]

def tptal_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])

def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    if start > (wg.vertex_count - 1) or start < 0:
        return None
    result: WeightedPath = [] # 最終的な MST を保持する。
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    visited: [bool] = [False] * wg.vertex_count # 訪問済みの場所を記録する。

    def visit(index: int):
        visited[index] = True # 訪問済みにする。
        for edge in wg.edges_for_index(index):
            # ここから出発して pq に至るすべて未訪問の edge を追加する。
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)

    while not pq.empty:
        edge = pq.pop()
        if visited[edge.v]:
            continue # 再訪しない。
        # これが今の最少なので、解に加える。
        result.append(edge)
        visit(edge.v) # ここにつながっているところに訪問する。

    return result

def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
        print(f"Total weight: {total_weight(wp)}")
