#!/usr/bin/python3
"""
script for a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """
        args:
            n (float): float
        Returns:
            floot: int
    """
    return math.floor(n)
