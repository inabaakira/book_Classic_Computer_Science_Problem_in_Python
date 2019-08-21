#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: maze.py
#    Created:       <2019/08/21 17:09:42>
#    Last Modified: <2019/08/21 17:26:24>

from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# from generic_search import dfs, bfs, node_to_path, astar, Node

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int
