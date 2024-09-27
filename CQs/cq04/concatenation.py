"""CQ04 Importing + Scope Assignment"""

__author__ = "730811558"


def concat(in1: str, in2: str) -> str:
    # combine two input strings
    return in1 + in2


# establish global variables for this file
word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":  # only runs the print when this file is called
    print(concat(word1, word2))
