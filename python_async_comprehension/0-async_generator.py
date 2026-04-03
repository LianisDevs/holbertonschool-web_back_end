#!/usr/bin/env python3
"""
async_generator module
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator()
    yields random num between 0-10 x10 and waits 1sec each time
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
