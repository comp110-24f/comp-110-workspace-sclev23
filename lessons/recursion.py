"""Practice with recursive functions."""


def factorial(n: int) -> int:
    """Compute the factorial of n."""
    # base case
    if n <= 1:
        return 1
    # recursive case
    else:
        return factorial(n - 1) * n


print(factorial(5))
