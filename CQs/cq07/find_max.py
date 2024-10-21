"""Unit Test Challenge Question."""

__author__ = "730811558"


def find_and_remove_max(nums: list[int]) -> int:
    """Find the largest num in a list and remove it from the list."""
    if nums == []:  # return -1 for empty list
        return -1
    big: int = nums[0]
    for i in nums:
        # find the largest num
        if i > big:
            big = i
    idx: int = 0
    # remove every instance of big from list
    while idx < len(nums):
        if nums[idx] == big:
            nums.pop(idx)
        else:
            idx += 1
    return big


a: list[int] = [1, 8, 2, 3, 3]
print(find_and_remove_max(a))
print(a)
