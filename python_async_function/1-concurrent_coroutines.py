#!/usr/bin/env python3
"""
concurrent module for use with wait_random module
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int, /) -> list[float]:
    """
    uses async to call wait_random function n times
    returns list of random delay times in sorted list
    """

    if not isinstance(n, int) or not isinstance(max_delay, int):
        return []

    return await asyncio.gather(*[
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)])
