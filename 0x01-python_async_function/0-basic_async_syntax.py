#!/usr/bin/env python3
"""
This module contains the this is wait_random method
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    this is wait_random method
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
