#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: word_search.py
#    Created:       <2020/10/22 13:58:58>
#    Last Modified: <2020/10/22 14:01:29>

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]

class GridLocation(NamedTuple):
    row: int
    column: int
