#!/usr/bin/env python3
"""
This module contains the wait_n method but for task 5
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    this is wait_n method
    """
    list_ = []
    for i in range(n):
        list_.append(await wait_random(max_delay))

    return sorted(list_)
