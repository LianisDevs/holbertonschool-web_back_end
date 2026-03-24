#!/usr/bin/env python3
"""This module contains make_multiplier function with typescripting"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """takes a float returns callable function to multipy by orig input"""

    def multiply(num: float):
        return multiplier * num

    return multiply
