#!/usr/bin/env python3
"""This module contains sum_list function with typescripting"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """adds list of floats together function"""
    result: float = 0

    for num in input_list:
        result += num

    return result
