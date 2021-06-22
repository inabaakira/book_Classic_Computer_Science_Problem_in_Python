#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: genetic_algorithm.py
#    Created:       <2021/06/22 11:12:37>
#    Last Modified: <2021/06/22 11:15:29>

from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean
from chromosome import Chromosome

C = TypeVar('C', bound=Chromosome)

class GenericAlgorithm(Generic[C]):
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")
