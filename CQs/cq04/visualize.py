from CQs.cq04.concatenation import concat  # imports the concat function
from CQs.cq04.coordinates import get_coords  # imports the get_coords function

"""CQ04 Importing + Scope Assignment"""

__author__ = "730811558"


# establish global variables for this file
x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
