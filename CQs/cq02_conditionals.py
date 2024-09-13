"""CQ2 Conditionals assignment."""

__author__ = "730811558"


def guess_a_number() -> None:
    """Have the user guess a number and see if it matches."""
    secret: int = 7
    response: str = input("Guess a number: ")  # recieve input as  a str
    print("Your guess was " + response)  # print response
    if int(response) > secret:
        print(
            "Your guess was too high! The secret number is " + str(secret)
        )  # turn secret into a str
    elif int(response) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("You got it!")
        # if response is not higher or lower than secret, then it must be secret


if __name__ == "__main__":
    guess_a_number()
