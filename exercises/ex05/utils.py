"""EX05 Utility Functions to Test."""

__author__ = "730811558"


def only_evens(num_list: list[int]) -> list[int]:
    """Returns a list of the even integers in num_list."""
    new_list: list[int] = []
    for i in num_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


def sub(num_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a subset of a list between certain indexes."""
    # start_idx is inclusive, end_idx is exclusive
    new_list: list[int] = []
    if len(num_list) == 0 or start_idx >= len(num_list) or end_idx <= 0:
        return []
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(num_list):
        end_idx = len(num_list)
    for i in range(start_idx, end_idx):
        new_list.append(num_list[i])
    return new_list


def add_at_index(num_list: list[int], elem: int, idx: int) -> None:
    """Places elem at the given idx."""
    if idx < 0 or idx > len(num_list):
        raise IndexError("Index is out of bounds for the input list")
    num_list.append(0)
    for i in range(len(num_list) - 1, idx, -1):
        # shift every number in the list 1 to the right
        num_list[i] = num_list[i - 1]
        print(num_list)
    num_list[idx] = elem
