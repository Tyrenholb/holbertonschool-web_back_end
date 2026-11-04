#!/usr/bin/env python3
"""Run multiple random-delay coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return random delays in the order their coroutines finish."""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(coroutines):
        delays.append(await coroutine)
    return delays
