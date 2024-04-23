#!/usr/bin/env python3
"""
This Module contains the async_generator coroutine
"""
import asyncio
import random


async def async_generator():
    """
    the async_generator coroutine
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
