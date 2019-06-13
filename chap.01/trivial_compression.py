#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: trivial_compression.py
#    Created:       <2019/06/13 20:47:40>
#    Last Modified: <2019/06/13 20:55:10>

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
