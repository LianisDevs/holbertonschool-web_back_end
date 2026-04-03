#!/usr/bin/env python3
"""
4-tasks module using task_wait_random()
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int, /) -> List[float]:
    """
    uses async to call task_wait_random function n times
    returns list of random delay times in sorted list
    """

    if not isinstance(n, int) or not isinstance(max_delay, int):
        return []

    if isinstance(n, bool) or isinstance(max_delay, bool):
        return []

    return await asyncio.gather(*[
        task_wait_random(max_delay) for _ in range(n)])
