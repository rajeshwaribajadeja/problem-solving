"""Array-2: fizz_buzz problem solution."""


def fizz_buzz(start: int, end: int) -> list:
    """Return strings from start to end with Fizz/Buzz substitutions.

    Consider the series of numbers beginning at start and running up to
    but not including end. Return a new array containing the string form
    of these numbers, except multiples of 3 are "Fizz", multiples of 5
    are "Buzz", and multiples of both 3 and 5 are "FizzBuzz".

    Args:
        start: Starting integer (inclusive).
        end: Ending integer (exclusive).

    Returns:
        A list of strings with FizzBuzz substitutions.

    Complexity:
        Time Complexity: O(N)
        Space Complexity: O(N)

    Examples:
        >>> fizz_buzz(1, 6)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> fizz_buzz(1, 8)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7']
        >>> fizz_buzz(1, 11)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
    """
    return [
        "FizzBuzz" if n % 15 == 0
        else "Fizz" if n % 3 == 0
        else "Buzz" if n % 5 == 0
        else str(n)
        for n in range(start, end)
    ]


if __name__ == "__main__":
    print(fizz_buzz(1, 6))
    print(fizz_buzz(1, 8))
    print(fizz_buzz(1, 11))
