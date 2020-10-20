#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: queens.py
#    Created:       <2020/10/20 15:21:49>
#    Last Modified: <2020/10/20 17:08:59>

if __name__ == "__main__":
    columns: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    rows: Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp: CSP[int, int] = CSP(columns, rows)
