#!/usr/bin/env python3

"""This module contains element_length function with typescripting"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """takes a list and returns item from list and length of item in tuple"""
    return [(i, len(i)) for i in lst]
