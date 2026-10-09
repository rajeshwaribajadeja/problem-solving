"""Warmup-2: string_times problem solution."""


def string_times(s: str, n: int) -> str:
    """Return a string that is n copies of the original string.

    Given a string and a non-negative int n, return a larger string
    that is n copies of the original string.

    Args:
        s: The input string.
        n: The non-negative number of copies.

    Returns:
        The resulting string repeated n times.

    Complexity:
        Time Complexity: O(L * n) where L is the length of string s.
        Space Complexity: O(L * n) to store the resulting repeated string.

    Examples:
        >>> string_times('Hi', 2)
        'HiHi'
        >>> string_times('Hi', 3)
        'HiHiHi'
        >>> string_times('Hi', 1)
        'Hi'
    """
    return s * n


if __name__ == "__main__":
    print(string_times("Hi", 2))
    print(string_times("Hi", 3))
    print(string_times("Hi", 1))