#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: network.py
#    Created:       <2021/12/06 11:03:00>
#    Last Modified: <2021/12/29 15:00:38>

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


    # 実際の出力と予測値との誤差から各 neuron での変化を計算する
    def backpropagate(self, expected: List[float]) -> None:
        # output layer neuron に対して delta を計算する
        last_layer: int = len(self.layers) - 1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        # hidden layers に対する delta を後ろから計算する
        for l in range(last_layer - 1, 0, 1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])

    # backpropagate() は weights を変更しない。
    # この関数は backpropagate() が計算した deltas を使って weights を変更する。
    def update_weights(self) -> None:
        for layer in self.layers[1:]: # input layer はスキップする。
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = \
                        neuron.weights[w] + \
                        ( neuron.learning_rate * \
                          (layer.previous_layer.output_cache[w]) * \
                          neuron.delta )

    # TODO: コメントを訳す．
    # train() uses the results of outputs() run over many inputs and compared
    # against expecteds to feed backpropagate() and update_weights()
    def train(self, inputs: List[List[float]], expecteds: List[List[float]]) -> None:
        for location, xs in enumerate(inputs):
            ys: List[float] = expecteds[location]
            outs: List[float] = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()
