#!/usr/bin/env python3
"""This module contains to_kv function with typescripting"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """takes a string and int or float and returns tuple function"""
    return (k, v ** 2)
