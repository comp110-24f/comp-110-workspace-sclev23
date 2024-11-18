"""Linked List Practice."""

from __future__ import annotations


class Node:
    """Node class basis."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializer."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
# print(one)
# print(courses)


def to_str(head: Node | None) -> str:
    """String path for Nodes."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# print(to_str(one))
# print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a Linked List."""
    # 1. If head is followed by None?
    #    Return head's value
    # 2. Else, return the last of the rest of the list (next Node)
    if head.next is None:
        return head.value  # Base case!
    else:
        return last(head.next)  # Recursive case!


# print(last(one))  # Expect 2
# print(last(courses))  # Expect 301


def r_range(start: int, end: int) -> Node | None:
    """Build a list recursively from start to end."""
    if start == end:
        return None
    elif start > end:
        raise ValueError("Invalid arguments")
    else:
        return Node(start, r_range(start + 1, end))


# print(r_range(9, 8))


def value_at(head: Node | None, index: int) -> int:
    """Returns the value of a Node at an index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.value
        else:
            return value_at(head.next, index - 1)


# print(value_at(Node(10, Node(20, Node(30, None))), 2))


def max(head: Node | None) -> int:
    """Returns the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    else:
        # initialize highest value
        high: int = head.value
        if head.next is None:
            # will only run at the end of the list
            return head.value
        else:
            # if the current frame value is greater than high, replace
            new: int = max(head.next)
            if new > high:
                high = new
        return high


# print(max(Node(30, Node(20, Node(10, None)))))


def linkify(items: list[int]) -> Node | None:
    """Return a linked list Node the same as a given list."""
    if len(items) <= 0:
        return None
    else:
        if len(items) == 1:
            return Node(items[0], None)
        else:
            return Node(items[0], linkify(items[1:]))


# print(linkify([1, 2, 3, 4, 1, 2]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Scale every value in a Node list by factor."""
    if head is None:
        return None
    else:
        if head.next is None:
            return Node(head.value * factor, None)
        else:
            return Node(head.value * factor, scale(head.next, factor))


print(scale(linkify([1, 2]), 2))
