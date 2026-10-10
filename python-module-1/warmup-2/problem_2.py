"""Warmup-2: front_times problem solution."""


def front_times(s: str, n: int) -> str:
    """Return n copies of the front 3 characters of a string.

    Given a string and a non-negative int n, we'll say that the front
    of the string is the first 3 chars, or whatever is there if the
    string is less than length 3. Return n copies of the front.

    Args:
        s: The input string.
        n: The non-negative number of copies.

    Returns:
        The front of the string repeated n times.

    Complexity:
        Time Complexity: O(n) (copies at most 3 characters n times).
        Space Complexity: O(n) to store the resulting string of length <= 3 * n.

    Examples:
        >>> front_times('Chocolate', 2)
        'ChoCho'
        >>> front_times('Chocolate', 3)
        'ChoChoCho'
        >>> front_times('Abc', 3)
        'AbcAbcAbc'
    """
    return s[:3] * n


if __name__ == "__main__":
    print(front_times("Chocolate", 2))
    print(front_times("Chocolate", 3))
    print(front_times("Abc", 3))