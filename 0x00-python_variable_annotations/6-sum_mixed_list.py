#!/usr/bin/env python3
"""
This module contais the sum_mixed_list method using typing annotaions
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum_mixed_list method
    """
    return sum(mxd_lst)
