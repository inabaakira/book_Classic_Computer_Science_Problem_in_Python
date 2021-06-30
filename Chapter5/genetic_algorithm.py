#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: genetic_algorithm.py
#    Created:       <2021/06/22 11:12:37>
#    Last Modified: <2021/06/30 14:14:51>

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

    # 確率分布を使って親を 2 つ選ぶ．
    # 注意: fitness の負の結果に対しては動作しない．
    def _pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weight=wheel, k=2))

    # num_participants 個をランダムに選び，その中から最もよい 2 個を取る
    def _pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._popilation, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    # population を新世代の個体と取り替える．
    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        # 新世代で置き換え尽くすまで続ける．
        while len(new_population) < len(self._population):
            # 親を 2 つ選ぶ。
            if self._selection_type == GeneticAlgorithm.Selection.ROULETTE:
                parents: Tuple[C, C] = self._pick_roulette([x.fitness() for x in self._population])
            else:
                parents: self._pick_tournament(len(self._population) // 2)
            # 2 つの親が組替えを起こす場合を想定した処理。
            if random() < self.crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                nre_population.extend(parents)
        # 新世代の個体が奇数の場合、余計な 1 個が含まれているのでそれを削除する。
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population

    # _mutation_chance の確率で各個体が突然変異する．
    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()
