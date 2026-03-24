#!/usr/bin/env python3
"""This module contains sum_mixed_list function with typescripting"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float, int]]) -> float:
    """adds list of floats together function"""
    result: float = 0

    for num in mxd_lst:
        result += num

    return result
