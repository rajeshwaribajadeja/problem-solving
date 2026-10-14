"""String-2: repeat_end problem solution."""


def repeat_end(s: str, n: int) -> str:
    """Return a string made of n repetitions of the last n characters.

    Given a string and an int n, return a string made of n repetitions
    of the last n characters of the string. Assume 0 <= n <= len(s).

    Args:
        s: The input string.
        n: The number of characters to take and repeat.

    Returns:
        A string of the last n characters repeated n times.

    Complexity:
        Time Complexity: O(n^2) to construct the repeated string.
        Space Complexity: O(n^2) to store the result.

    Examples:
        >>> repeat_end("Hello", 3)
        'llollollo'
        >>> repeat_end("Hello", 2)
        'lolo'
        >>> repeat_end("Hello", 1)
        'o'
    """
    return s[-n:] * n if n > 0 else ""


if __name__ == "__main__":
    print(repeat_end("Hello", 3))
    print(repeat_end("Hello", 2))
    print(repeat_end("Hello", 1))
