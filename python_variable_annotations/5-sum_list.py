#!/usr/bin/env python3
"""This module contains sum_list function with typescripting"""


def sum_list(input_list: list[float]) -> float:
    """adds list of floats together function"""
    result: float = 0

    for num in input_list:
        result += num

    return result
