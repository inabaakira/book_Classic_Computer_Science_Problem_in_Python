#!/usr/bin/env python3
#-*- mode: python; coding: utf-8 -*-
# file: unbreakable_encryption.py
#    Created:       <2019/07/25 00:51:35>
#    Last Modified: <2019/07/25 00:53:39>

from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")
