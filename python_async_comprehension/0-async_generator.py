#!/usr/bin/env python3
"""Generate random numbers asynchronously."""

import asyncio
import random


async def async_generator():
    """Yield 10 random floats between 0 and 10, waiting one second before each."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
