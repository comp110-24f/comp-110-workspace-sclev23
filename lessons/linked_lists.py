"""Linked List Practice."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
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


def to_str(head: Node | None):
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


print(r_range(9, 8))
