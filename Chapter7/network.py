#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: network.py
#    Created:       <2021/12/06 11:03:00>
#    Last Modified: <2021/12/06 22:12:45>

from __future__ import anootations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid

T = TypeVar('T') # neural network が解釈した出力

class Network:
    def __init__(self,
                 layer_structure: List[int],
                 learning_rate: float,
                 activation_function: Callable[[float], float] = sigmoid,
                 derivative_activation_function: Callable[[float], float] = derivative_sigmoid) \
                 -> None:
        if len(layer_structure) < 3:
            raise ValueError("Error: Should be at least 3 layers (1 input, 1 hidden, 1 output)")
        self.layers: List[Layer] = []
        # input layer
        input_layer: Layer = Layer(None,
                                   layer_structure[0],
                                   learning_rate,
                                   activation_function,
                                   derivative_activation_function)
        self.layers.append(input_layer)
        # hidden layer and output layer
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.leyers[previous],
                               num_neurons,
                               learning_rate,
                               activation_function,
                               derivative_activation_function)
            self.leyers.append(next_layer)

    # 入力値を first layer に与えると first layer の出力は second layer の入力に，
    # second layer の出力は third layer の入力となる．その後も同様．
    def outputs(self, input: List[float]) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs), self.layers, input)
