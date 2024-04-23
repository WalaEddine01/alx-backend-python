#!/usr/bin/env python3
"""
This Module contains the async_comprehension coroutine
"""
import asyncio
import random
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    the async_generator coroutine
    """
    random_numbers = [value async for value in async_generator()]
    return random_numbers
