#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: layer.py
#    Created:       <2021/11/22 17:12:13>
#    Last Modified: <2021/11/22 23:24:55>

from __future__ import annotations
from typing import List, Callable, Optional
from random import random
from neuron import Neuron
from util import dot_product

class Layer:
    def __init__(self,
                 previous_layer: Optional[Layer],
                 num_neurons: int,
                 learning_rate: float,
                 activation_function: Callable[[float], floet],
                 derivative_activation_function: Callable[[float], float]) -> None:
        self.previous_layer: Optional[Layer] = previous_layer
        self.neurons: List[Neuron] = []
        # 次によって単一の大きなリストに包含される
        for i in range(num_neurons):
            if previous_layer is None:
                random_weights: List[float] = []
            else:
                random_weights = [random() for _ in range(len(previous_layer.neurons))]
            neuron: Neuron = Neuron(random_weights,
                                    learning_rate,
                                    activation_function,
                                    derivative_activation_function)
            self.neurons.append(neuron)
        self.output_cache: List[float] = [0.0 for _ in range(num_neurons)]

    def outputs(self, inputs: List[float]) -> List[float]:
        if self.previous_layer is None:
            self.output_cache = inputs
        else:
            self.output_cache = [n.output(inputs) for n in self.neurons]
        return self.output_cache
