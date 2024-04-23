#!/usr/bin/env python3
"""
This Module contains the measure_runtime coroutine
"""
import asyncio
import random
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    the measure_runtime coroutine
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
