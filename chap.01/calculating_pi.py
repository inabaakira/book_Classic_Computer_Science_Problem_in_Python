#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: calculating_pi.py
#    Created:       <2019/07/28 14:36:16>
#    Last Modified: <2019/07/28 14:39:00>

def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    print(calculate_pi(1000000))
