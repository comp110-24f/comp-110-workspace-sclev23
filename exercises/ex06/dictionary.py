"""Exercise 06 Dictionary Utils."""

__author__ = "730811558"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Swaps the key-values of a given dictionary."""
    new_dict: dict[str, str] = {}
    # iterate through every key in given
    for i in given:
        if given[i] in new_dict:
            # if value at current index is already present in new_dict
            raise KeyError("Cannot have duplicate values to keys.")
        else:
            new_dict[given[i]] = i
    return new_dict


# print(invert({"kris": "jordan", "michael": "y", "jordan": "c"}))


def favorite_color(given: dict[str, str]) -> str:
    """Returns the most popular favorite color from a dictionary."""
    if given == {}:
        return ""
    color_count: dict[str, int] = {}
    for i in given:
        if given[i] in color_count:
            # if current color present in color_count, add 1
            color_count[given[i]] += 1
        else:
            # else, initialize new key-value as 1
            color_count[given[i]] = 1
    print(color_count)
    first: bool = True
    # initialzing a biggest variable since it's hard to index a dict
    popular: str = ""
    biggest_num: int = 0
    for i in color_count:
        if first is True:
            # set the first item to be the biggest number
            biggest_num = color_count[i]
            # also set as the most populat color
            popular = i
            first = False
            # ensure this does not iterate again
        current_num: int = color_count[i]
        if current_num > biggest_num:
            # set biggest_num to be current_num and get new popular color
            biggest_num = current_num
            popular = i
    return popular


# print(favorite_color({"John": "blue"}))

"""
print(
    favorite_color(
        {
            "Marc": "green",
            "Ezri": "blue",
            "Kris": "red",
            "Kate": "blue",
            "Thomas": "green",
            "Greg": "blue",
            "Bob": "red",
            "Beth": "red",
        }
    )
)
It looks like this because I had to do extensive testing,
this one was a doozey...
"""


def count(given: list[str]) -> dict[str, int]:
    """Returns a dict with values from a list and how many times they appear."""
    count_dict: dict[str, int] = {}
    for i in given:
        if i in count_dict:
            # if i is found in count_dict, add an occurence
            count_dict[i] += 1
        else:
            # else, create new key and set to 1 occurence
            count_dict[i] = 1
    return count_dict


# print(count(["one", "two", "one", "four", "two"]))


def alphabetizer(given: list[str]) -> dict[str, list[str]]:
    """Returns every element of a list as a dict by letter."""
    alpha_dict: dict[str, list[str]] = {}
    for i in given:
        if i[0].lower() in alpha_dict:
            # if the first letter in i is a key in alpha_dict, append i to list
            alpha_dict[i[0].lower()].append(i)
        else:
            # else, create new key and create new list
            alpha_dict[i[0].lower()] = [i]
    return alpha_dict


# print(alphabetizer(["Python", "sugar", "Turtle", "party", "table"]))


def update_attendance(given: dict[str, list[str]], day: str, student: str) -> None:
    """Modifies and returns an attendance dict with a student on a given day."""
    if day in given:
        # only append student if student is NOT already in given[day]
        if student not in given[day]:
            given[day].append(student)
        else:
            return None
    else:
        # otherwise add student to new day
        given[day] = [student]
    return None


"""
attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
print(attendance_log)
update_attendance(attendance_log, "Tuesday", "Vrinda")
print(attendance_log)
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)
update_attendance(attendance_log, "Monday", "Kaleb")
print(attendance_log)
"""
