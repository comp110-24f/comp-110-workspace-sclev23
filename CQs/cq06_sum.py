"""Summing the elements of a list using different loops."""

__author__ = "730811558"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all items in list."""
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


# print(w_sum([1.5, 0.4, 1.0]))


def f_sum(vals: list[float]) -> float:
    """Returns sum of all items in list using for loop."""
    sum: float = 0
    for i in vals:
        sum += i
    return sum


# print(f_sum([1.9, 0.9, 1.0]))


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of all items in list using for in range loop."""
    sum: float = 0
    for i in range(0, len(vals)):
        # specify the the index of vals at i
        sum += vals[i]
    return sum


print(f_range_sum([1.1, 0.4, 1.0]))
