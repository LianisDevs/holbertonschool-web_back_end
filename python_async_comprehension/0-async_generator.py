#!/usr/bin/env python3
"""
async_generator module
"""

import asyncio
import random


async def async_generator():
    """
    async_generator()
    yields random num between 0-10 x10 and waits 1sec each time
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
