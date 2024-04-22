#!/usr/bin/env python3
'''
This module contains method called measure_time
'''
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    this is the measure_time function
    """
    total_time = 0
    delay = asyncio.run(wait_n(n, max_delay))
    for i in delay:
        total_time += i

    return total_time / n
