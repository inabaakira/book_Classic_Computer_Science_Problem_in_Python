#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: mst.py
#    Created:       <2021/01/23 23:38:42>
#    Last Modified: <2021/02/02 23:21:57>

from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue

V = TypeVar('V')
WeightedPath = List[WeightedEdge]

def total_weight(wp: WeightedPath) -> float:
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
            # ここから出発して pq に至るすべての未訪問の edge を追加する。
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)

    while not pq.empty:
        edge = pq.pop()
        if visited[edge.v]:
            continue # 再訪しない。
        # これが今の最小なので、解に加える。
        result.append(edge)
        visit(edge.v) # ここにつながっているところに訪問する。

    return result

def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f"{wg.vertex_at(edge.u)} {edge.weight}> {wg.vertex_at(edge.v)}")
    print(f"Total weight: {total_weight(wp)}")

if __name__ == "__main__":
    city_graph2: WeightedGraph[str] = WeightedGraph([
        "Seattle", "San Francisco", "Los Angels", "Riverside",    "Phoenix",
        "Chicago", "Boston",        "New York",   "Atlanta",      "Miami",
        "Dallas",  "Houston",       "Detroit",    "Philadelphia", "Washington"
    ])

    city_graph2.add_edge_by_vertices("Seattle",       "Chicago",       1737)
    city_graph2.add_edge_by_vertices("Seattle",       "San Francisco",  678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside",      386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angels",     348)
    city_graph2.add_edge_by_vertices("Los Angels",    "Riverside",       50)
    city_graph2.add_edge_by_vertices("Los Angels",    "Phoenix",        357)
    city_graph2.add_edge_by_vertices("Riverside",     "Phoenix",        307)
    city_graph2.add_edge_by_vertices("Riverside",     "Chicago",       1704)
    city_graph2.add_edge_by_vertices("Phoenix",       "Dallas",         887)
    city_graph2.add_edge_by_vertices("Phoenix",       "Houston",       1015)
    city_graph2.add_edge_by_vertices("Dallas",        "Chicago",        805)
    city_graph2.add_edge_by_vertices("Dallas",        "Atlanta",        721)
    city_graph2.add_edge_by_vertices("Dallas",        "Houston",        225)
    city_graph2.add_edge_by_vertices("Houston",       "Atlanta",        702)
    city_graph2.add_edge_by_vertices("Houston",       "Miami",          968)
    city_graph2.add_edge_by_vertices("Atlanta",       "Chicago",        588)
    city_graph2.add_edge_by_vertices("Atlanta",       "Washington",     543)
    city_graph2.add_edge_by_vertices("Atlanta",       "Miami",          604)
    city_graph2.add_edge_by_vertices("Miami",         "Washington",     923)
    city_graph2.add_edge_by_vertices("Chicago",       "Detroit",        238)
    city_graph2.add_edge_by_vertices("Detroit",       "Boston",         613)
    city_graph2.add_edge_by_vertices("Detroit",       "Washington",     396)
    city_graph2.add_edge_by_vertices("Detroit",       "New York",       482)
    city_graph2.add_edge_by_vertices("Boston",        "New York",       190)
    city_graph2.add_edge_by_vertices("New York",      "Philadelphia",    81)
    city_graph2.add_edge_by_vertices("Philadelphia",  "Washington",     123)

    result: Optional[WeightedPath] = mst(city_graph2)
    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(city_graph2, result)
