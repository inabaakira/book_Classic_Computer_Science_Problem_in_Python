#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: map_coloring.py
#    Created:       <2020/10/16 14:06:13>
#    Last Modified: <2020/10/16 18:38:24>

from csp import Constraint, CSP
from typing import Dict, List, Optional

class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1] != assignment[self.place2]
