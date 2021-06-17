#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: chromosome.py
#    Created:       <2021/06/17 16:06:22>
#    Last Modified: <2021/06/17 16:51:51>

from __future__ import annotations
from typing import TypeVar, Tuple, Type
from abc import ABC, abstractmethod

T = TypeVar('T', bound='Chromosome')

# 全 chromosomes の基底クラス; 全てのメソッドは override される。
class Chromosome(ABC):
    @abstractmethod
    def fitness(self) -> float:
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls: Type[T]) -> T:
        ...

    @abstractmethod
    def crossover(self: T, other: T) -> Tuple[T, T]:
        ...

    @abstractmethod
    def mutate(self) -> None:
        ...
