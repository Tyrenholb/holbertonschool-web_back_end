#!/usr/bin/env python3
"""A corotuine that loops 10 times and waits 1 second"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Pass no arguements to it, useses random."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
