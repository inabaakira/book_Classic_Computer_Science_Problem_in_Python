#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: csp.py
#    Created:       <2020/10/07 17:43:35>
#    Last Modified: <2020/10/09 11:41:11>

from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')
D = TypeVar('D')

class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        ...
