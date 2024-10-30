"""Summing the elements of a list using different loops"""

__author__ = "730771663"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    if len(vals) == 0:
        return 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return float(round(sum))


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for x in vals:
        sum = sum + x
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    index: int = 0
    if len(vals) == 0:
        return 0.0
    for index in range(0, len(vals)):
        sum = sum + vals[index]
    return sum
