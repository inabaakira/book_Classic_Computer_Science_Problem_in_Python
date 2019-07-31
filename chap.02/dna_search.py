#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: dna_search.py
#    Created:       <2019/07/31 20:40:40>
#    Last Modified: <2019/07/31 21:21:24>

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # type alias for codons
Gene = List[Codon] # type alias for genes
