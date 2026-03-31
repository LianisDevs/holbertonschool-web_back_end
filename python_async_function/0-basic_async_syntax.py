#!/usr/bin/env python3
"""basic async module"""

import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    generates random number
    waits random number delay
    returns random number
    """
    random_num = random.uniform(0, max_delay)
    time.sleep(random_num)
    return random_num
