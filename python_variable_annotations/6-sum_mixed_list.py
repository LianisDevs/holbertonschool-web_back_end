#!/usr/bin/env python3
"""This module contains sum_mixed_list function with typescripting"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """adds list of floats together function"""
    result: float = 0

    for num in mxd_lst:
        result += num

    return result
