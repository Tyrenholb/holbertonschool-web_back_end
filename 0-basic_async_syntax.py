#!/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random delay and return it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
