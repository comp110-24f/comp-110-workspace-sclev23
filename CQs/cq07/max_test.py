from CQs.cq07.find_max import find_and_remove_max

"""Unit Test Challenge Question."""

__author__ = "730811558"


def test_find_and_remove_max_ret() -> None:
    """Test that the function returns correctly."""
    b: list[int] = [9, 8, 6, 10, 4, 11, 5, 11]
    assert find_and_remove_max(b) == 11


def test_find_and_remove_max_mut() -> None:
    """Test that the list gets mutated correctly."""
    b: list[int] = [1, 8, 2, 3, 3]
    find_and_remove_max(b)
    assert b == [1, 2, 3, 3]


def test_find_and_remove_max_edge() -> None:
    """Test that the function works with an empty list."""
    assert find_and_remove_max([]) == -1
