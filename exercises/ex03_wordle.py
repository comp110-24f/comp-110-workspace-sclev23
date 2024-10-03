"""EX03 Wordle exercise."""

__author__ = "730811558"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def input_guess(secret_word_len: int) -> str:
    """Gets a a guess input and ensures it's the correct length."""
    guess = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guess) != secret_word_len
    ):  # while the length of guess does NOT equal the secret word length
        print(f"That wasn't {secret_word_len} chars! Try again: ")
        guess = (
            input()
        )  # I couldn't figure out how to get the guess on the same line as the message
    return guess


def contains_char(secret_word: str, char: str) -> bool:
    """Returns a bool if char is found in secret_word"""
    assert len(char) == 1
    idx = 0
    found_char = False
    while idx < len(secret_word):
        if char == secret_word[idx]:
            found_char = True  # only return true if any char is found in secret_word
        idx += 1
    return found_char


def emojified(user_guess: str, secret_word: str) -> str:
    """Emojifies the user guess to the secret word like wordle."""
    assert len(user_guess) == len(secret_word)
    idx = 0
    concat_boxes = ""  # initialize an empty string for boxes
    while idx < len(secret_word):
        if (
            user_guess[idx] == secret_word[idx]
        ):  # if current guess index matches currnet secret index
            concat_boxes += GREEN_BOX
            idx += 1
        elif contains_char(
            secret_word=secret_word, char=user_guess[idx]
        ):  # if a character is present in the string
            concat_boxes += YELLOW_BOX
            idx += 1
        else:  # if nothing is present anywhere
            concat_boxes += WHITE_BOX
            idx += 1
    return concat_boxes


def main(secret: str) -> None:
    """Meat and potatoes, ties everything into the game."""
    turn = 1
    win = False
    while turn <= 6 and win is False:  # while you still have turns and you haven't won
        print(f"=== Turn {turn}/6 ===")
        current_guess = input_guess(
            len(secret)
        )  # ensures the guess is as long as the secret word
        print(
            emojified(current_guess, secret)
        )  # prints the emoji concat for the guess to the secret
        if current_guess == secret:
            win = True
        else:
            turn += 1
    # determines if you won after the 6 turn loop ends
    if win is True:
        print(f"You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
