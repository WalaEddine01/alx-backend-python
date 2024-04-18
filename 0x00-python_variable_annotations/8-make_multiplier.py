#!/usr/bin/env python3
"""
This module contais the make_multiplier  method using typing annotaions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier method
    """
    def mul(numFloat: float) -> float:
        """
        the mul method
        """
        return numFloat * multiplier
    return mul
