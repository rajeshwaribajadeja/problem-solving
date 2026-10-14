"""Logic-1: fizz_string2 problem solution."""


def fizz_string2(n: int) -> str:
    """Return the string form of n followed by '!', or 'Fizz!', 'Buzz!',
    'FizzBuzz!'.

    Given an int n, return the string form of the number followed by "!".
    Except if the number is divisible by 3 use "Fizz" instead of the number,
    and if the number is divisible by 5 use "Buzz", and if divisible by
    both 3 and 5, use "FizzBuzz".

    Args:
        n: An integer.

    Returns:
        "Fizz!", "Buzz!", "FizzBuzz!", or "{n}!".

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> fizz_string2(1)
        '1!'
        >>> fizz_string2(2)
        '2!'
        >>> fizz_string2(3)
        'Fizz!'
    """
    return (
        "FizzBuzz!" if n % 15 == 0
        else "Fizz!" if n % 3 == 0
        else "Buzz!" if n % 5 == 0
        else f"{n}!"
    )


if __name__ == "__main__":
    print(fizz_string2(1))
    print(fizz_string2(2))
    print(fizz_string2(3))