#!/usr/bin/env python3
"""
This module contais the element_length method using typing annotaions
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    element_length method
    """
    return [(i, len(i)) for i in lst]
