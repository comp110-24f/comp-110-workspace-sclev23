import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""EX05 Utility Function Testing."""

__author__ = "730811558"


def test_only_evens_edge() -> None:
    """Tests for an empty list."""
    my_list: list[int] = []
    assert only_evens(my_list) == []


def test_only_evens_use_ret() -> None:
    """Tests for normal return val."""
    my_list: list[int] = [1, 3, 4, 5, -4, 6, 7, 8, 2, 9, -10, 11]
    assert only_evens(my_list) == [4, -4, 6, 8, 2, -10]


def test_only_evens_use_not_mut() -> None:
    """Tests for no mutation of list."""
    my_list: list[int] = [1, 3, 5, 7, 9]
    only_evens(my_list)
    assert my_list == [1, 3, 5, 7, 9]


def test_sub_edge() -> None:
    """Tests for out of range indexes."""
    my_list: list[int] = [1, 2, 4, 5, 6, 8, 9, 13]
    assert sub(my_list, 13, 0) == []


def test_sub_use_ret() -> None:
    """Tests for normal return val."""
    my_list: list[int] = [1, 3, 5, 12, 95, 11, 42, 7, 19]
    assert sub(my_list, 2, 7) == [5, 12, 95, 11, 42]


def test_sub_use_not_mut() -> None:
    """Tests for no mutation of list."""
    my_list: list[int] = [1, 3, 5, 12, 95, 11, 42, 7, 19]
    sub(my_list, -45, 20)
    assert my_list == [1, 3, 5, 12, 95, 11, 42, 7, 19]


def test_add_at_index_edge() -> None:
    """Test for an in range index."""
    my_list: list[int] = [1, 2, 3, 4, 5, 6]
    with pytest.raises(IndexError):
        add_at_index(my_list, 25, 20)


def test_add_at_index_ret() -> None:
    """Tests for normal return val."""
    my_list: list[int] = [1, 4, 29, 8, 52, 29, 13, 40]
    assert add_at_index(my_list, 17, 4) is None


def test_add_at_index_use_mut() -> None:
    """Tests for normal list mutation."""
    my_list: list[int] = [1, 4, 29, 8, 52, 29, 13, 40]
    add_at_index(my_list, 17, 4)
    assert my_list == [1, 4, 29, 8, 17, 52, 29, 13, 40]
