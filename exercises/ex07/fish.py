"""File to define Fish class."""

__author__ = "730811558"


class Fish:
    """A fish with an age."""

    age: int

    def __init__(self):
        """Initialize new fish."""
        self.age = 0

    def one_day(self):
        """One day for a fish."""
        self.age += 1
