#!/usr/bin/env python3
"""
This module contains the wait_n method
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    list_ = []
    for i in range(n):
        list_.append(await wait_random(max_delay))

    return list_
