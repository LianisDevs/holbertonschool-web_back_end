#!/usr/bin/env python3
"""
measure_runtime module using async_comprehension()
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime()
    measures total time of running async_comprehension() x 4
    """
    start_time = time.time()
    # execute async_comprehension four times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
