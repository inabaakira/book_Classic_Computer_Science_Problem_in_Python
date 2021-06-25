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

    def __init__(self,
                 initial_population: List[C],
                 threshold: float,
                 max_generations: int = 100,
                 mutation_chance: float = 0.01,
                 crossover_chance: float = 0.7,
                 selection_type: SelectionType.TOURNAMENT) -> None:
        self._population: List[C] = initial_population
        self._threshold: float = threshold
        self._max_generations: int = max_generations
        self._mutation_chance: float = mutation_chance
        self._crossover_chance: float = crossover_chance
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type
        self._fitness_key: Callable = type(self._population[0]).fitness

