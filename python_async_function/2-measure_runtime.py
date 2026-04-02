#!/usr/bin/env python3
"""measure_time module for async functions"""

import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int, /) -> float:
    """
    measures the total_time for completing wait_n()
    divides total_time by n for average time
    """

    start_time = time.time()

    await wait_n(n, max_delay)

    end_time = time.time()

    total_time = (end_time - start_time) / n

    return total_time
