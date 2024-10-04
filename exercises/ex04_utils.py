"""EX04 List Utils Exercise."""

__author__ = "730811558"


def all(num_list: list[int], num: int) -> bool:
    """Returns True if num matches all indices in num_list."""
    if len(num_list) == 0:
        return False
    idx: int = 0
    matches: int = 0
    while idx < len(num_list):
        if num_list[idx] == num:  # if indicie matches num, add 1 to macthes
            matches += 1
        idx += 1
    if matches == len(num_list):
        # if by the end the number of matches == the length of list, evry indicie is num
        return True
    else:
        return False


def max(num_list: list[int]) -> int:
    """Finds the highest number in a list."""
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    mnum: int = num_list[0]  # initialize highest number
    idx: int = 0
    while idx < len(num_list):
        # if current index is higher than current high number, change high number
        if num_list[idx] > mnum:
            mnum = num_list[idx]
        idx += 1
    return mnum


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if two lists are exactly equal."""
    idx: int = 0
    matches: int = 0
    while idx < len(list1) and idx < len(
        list2
    ):  # while idx is less than length of both lists
        if list1[idx] == list2[idx]:
            matches += 1
        idx += 1
    if matches == len(list1) and matches == len(
        list2
    ):  # if matches == length of both lists, return True
        return True
    else:
        return False


def extend(list1: list[int], list2: list[int]) -> None:
    """Append list2 to the end of list1."""
    idx: int = 0
    while idx < len(list2):
        # while idx < lenght of list2, append index
        list1.append(list2[idx])
        idx += 1


a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
c: list[int] = [7, 8]
extend(c, b)
print(c)
