"""File to define Bear class."""

__author__ = "730811558"


class Bear:
    """A bear with an age and hunger_score."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initilaize new bear."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """One day for a bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Bear eating fish."""
        self.hunger_score += num_fish
