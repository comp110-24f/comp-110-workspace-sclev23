"""My first CQ in COMP110"""

__author__ = "730811558"


def mimic(message: str) -> str:
    """Take input and repeat it back to you."""
    return message


def main() -> None:
    """Print the result of calling mimic  func."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
