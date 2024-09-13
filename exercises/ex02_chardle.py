"""EX02 Chardle assignment."""

__author__ = "730811558"


def input_word() -> str:
    """Test the length of an input from the user to be 5."""
    user_word: str = input("Enter a 5-character word: ")  # takes input as a string
    if len(user_word) != 5:  # if the length of user_word does not equal 5
        print("Error: Word must contain 5 characters.")
        exit()
        return user_word
    else:
        return user_word


def input_letter() -> str:
    """Asks for a letter to search in user_word."""
    user_letter: str = input("Enter a single character: ")  # takes input as a string
    if len(user_letter) != 1:  # if the lenght of user_eltter does not equal 1
        print("Error: Character must be a single character.")
        exit()
        return user_letter
    else:
        return user_letter


def contains_char(word: str, letter: str) -> None:
    """Checks for letter at every indicie in word."""
    count: int = 0  # initialize count variable
    print("Searching for " + letter + " in " + word)
    # absolutely nasty wall of ifs checking for instances of letter in word
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    # print results based on count
    if count < 1:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Main tying function."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
