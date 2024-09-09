"""Conditionals Practice."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    if num < 10:  # check if this is true
        print("Small number!")  # "then" block
    else:
        print("Big number!")
    print("This is the end of the function!")


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to COMP110!"
    else:
        return "Keep sleeping!"


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter matches the first letter of a word."""
    if word[0] == letter:  # if the first character in word is letter
        return "Match!"
    else:
        return "No Match!"


print(check_first_letter(word="sappy", letter="h"))
