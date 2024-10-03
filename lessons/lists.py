"""Basic syntax of lists."""

my_numbers: list[float] = []
# my_numbers: list[float] = list() <- with a constructor

# Add an itme to a list
my_numbers.append(1.5)
my_numbers.append(2.3)

# Create an already populated list
game_points: list[int] = [102, 86, 94]

# Modifying elements
game_points[1] = 72

# Get length
len(game_points)  # = 3

# Remove an element
# game_points.pop(1)

# Write a function called display
# Input: list[int]
# Return Value: None
# Loop over the input and print every value
# Try calling it on game_points!


def display(exlist: list[int]) -> None:
    idx: int = 0
    while idx < len(exlist):
        print(exlist[idx])
        idx += 1


display(game_points)
game_points.append(94)
print(game_points)

"""
Self practice using for

def display2(exlist: list[int]) -> None:
    for i in exlist:
        print(i)


display2(game_points)
"""
