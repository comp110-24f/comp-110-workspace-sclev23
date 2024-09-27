"""CQ03 While Loops Assingment"""

__author__ = "730811558"


def num_instances(phrase: str, search_char: str) -> int:
    """Count the number of instances search_char appears in phrase."""
    count: int = 0  # initalize counter
    i = 0  # initialize index
    while i < len(phrase):  # while index is less than the lenght of phrase
        if search_char == phrase[i]:
            # if character matches, add 1 to counter
            count += 1
        i += 1  # always add 1 to the index
    return count


print(num_instances(phrase="Happy Tuesday!", search_char="z"))
# phrase can be any string and search_char should be a single character
