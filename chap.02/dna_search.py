#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: dna_search.py
#    Created:       <2019/07/31 20:40:40>
#    Last Modified: <2019/08/03 18:07:29>

from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # type alias for codons
Gene = List[Codon] # type alias for genes

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # don't run off end!
            return gene
        # initialize codon out of three nuleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon) # add codon to gene
    return gene

my_gene: Gene = string_to_gene(gene_str)
