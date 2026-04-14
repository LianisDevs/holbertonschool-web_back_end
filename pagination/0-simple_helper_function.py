#!/usr/bin/env python3
"""
simple-helper function module
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Parameters: page and page_size
    Return: tuple of (start index, end index)
    """
    # pages are 1-indexed but data is 0-indexed so page - 1
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
