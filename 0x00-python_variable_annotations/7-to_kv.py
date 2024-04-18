#!/usr/bin/env python3
"""
This module contais the sum_mixed_list method using typing annotaions
"""
from typing import Tuple


def to_kv(k: str, v: float | int) -> Tuple:
    """
    to_kv method
    """
    return (k, float((v * v)))
