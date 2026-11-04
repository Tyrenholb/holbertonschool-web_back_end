#!/usr/bin/env python3
"""Measure the runtime of four async comprehensions."""

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return the time taken to run four comprehensions concurrently."""
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    finish_time = time.perf_counter()
    total_time = finish_time - start_time
    return total_time
