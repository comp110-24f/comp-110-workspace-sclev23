"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730811558"


class River:
    """The main river that counts days, number of fish, and number of bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Updates fish and bears based on age."""
        # remove any fish over 3 days old
        new_fish: list[Fish] = []
        for i in self.fish:
            if i.age <= 3:
                new_fish.append(i)
        self.fish = new_fish
        # removie any bears over 5 days old
        new_bears: list[Bear] = []
        for i in self.bears:
            if i.age <= 5:
                new_bears.append(i)
        self.bears = new_bears

    def remove_fish(self, amount: int):
        """Removes an amount of fish from the front of the list."""
        for i in range(0, amount):
            self.fish.pop(i)

    def bears_eating(self):
        """If there are more than 5 fish, every bear eats 3 fish."""
        for i in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                i.eat(3)

    def check_hunger(self):
        """Removes any bears with a hunger score < 0."""
        new_bears: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                new_bears.append(i)
        self.bears = new_bears

    def repopulate_fish(self):
        """Adds 4 new fish for every 2 fish."""
        more_fish: list[Fish] = []
        for i in range(1, len(self.fish), 2):
            for d in range(0, 4):
                more_fish.append(Fish())
        for d in more_fish:
            self.fish.append(d)

    def repopulate_bears(self):
        """Adds new bear for every 2 bears."""
        more_bears: list[Bear] = []
        for i in range(1, len(self.bears), 2):
            more_bears.append(Bear())
        for d in more_bears:
            self.bears.append(d)

    def view_river(self):
        """Print the populations and day of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        for i in range(0, 7):
            self.one_river_day()
