"""Warmup-1: front22 problem solution."""


def front22(s: str) -> str:
    """Take the first 2 characters and add them at the front and back.

    Given a string, take the first 2 chars and return the string with
    the 2 chars added at both the front and back. If the string length
    is less than 2, use whatever chars are there.

    Args:
        s: The input string.

    Returns:
        The string wrapped by its first 2 characters.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the new string of length N + 4.

    Examples:
        >>> front22("kitten")
        'kikittenki'
        >>> front22("Ha")
        'HaHaHa'
        >>> front22("abc")
        'ababcab'
    """
    return s[:2] + s + s[:2]


if __name__ == "__main__":
    print(front22("kitten"))
    print(front22("Ha"))
    print(front22("abc"))