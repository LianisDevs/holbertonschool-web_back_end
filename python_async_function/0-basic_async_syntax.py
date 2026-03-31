#!/usr/bin/env python3
"""basic async module"""

import random
import asyncio


async def wait_random(max_delay=10):
    """
    generates random number
    waits random number delay
    returns random number
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
