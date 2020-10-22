#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: word_search.py
#    Created:       <2020/10/22 13:58:58>
#    Last Modified: <2020/10/22 15:14:54>

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]

class GridLocation(NamedTuple):
    row: int
    column: int

def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid: Grid):
    for row in grid:
            print("".join(row))
