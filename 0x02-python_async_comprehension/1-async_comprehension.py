#!/usr/bin/env python3
"""
This Module contains the async_comprehension coroutine
"""
import asyncio
import random
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    result = []
    for i in async_generator():
        result.append(i)

    return result
