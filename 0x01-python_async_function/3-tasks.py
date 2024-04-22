#!/usr/bin/env python3
"""
This module contains the task_wait_random
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    this is the task_wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))
