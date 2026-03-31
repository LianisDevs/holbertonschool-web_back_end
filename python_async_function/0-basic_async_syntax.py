#!/usr/bin/env python3

import random
import asyncio


async def wait_random(max_delay=10):
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
