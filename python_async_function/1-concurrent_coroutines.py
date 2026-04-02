#!/usr/bin/env python3
"""concurrent module"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    uses async to call wait_random function n times
    returns list of random delay times in sorted list
    """

    if not isinstance(n, int) or isinstance(n, bool) or \
            isinstance(max_delay, bool):
        return [0.0]

    delay_list = []

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for completed in asyncio.as_completed(tasks):
        result = await completed
        delay_list.append(result)

    return delay_list
