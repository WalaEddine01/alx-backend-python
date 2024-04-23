#!/usr/bin/env python3
"""
This Module contains the async_generator coroutine
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    the async_generator coroutine
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
