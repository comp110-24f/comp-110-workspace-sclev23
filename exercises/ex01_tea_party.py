"""Tea party exercise."""

__author__ = "730811558"


def main_planner(guests: int) -> None:
    """The main calculating function, print all of the text."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # prints a string for the amount of people
    print("Tea Bags: " + str(tea_bags(people=guests)))  # prints the amount of tea bags
    print("Treats: " + str(treats(people=guests)))  # prints the amount of treats
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )  # the amount of tea bags and the amount of treats put into the cost function
    )


def tea_bags(people: int) -> int:
    """Calculate 2 tea bags per guest."""
    return people * 2


def treats(people: int) -> int:
    """Calculate 1.5 treats per drink."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of tea and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party?"))
    )  # asks for user input for amount of people
