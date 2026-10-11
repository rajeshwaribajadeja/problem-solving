"""String-1: middle_three problem solution."""


def middle_three(s: str) -> str:
    """Return a string of length 3 from the middle of an odd-length string.

    Given a string of odd length, return the string length 3 from its
    middle, so "Candy" yields "and". The string length will be at least 3.

    Args:
        s: An odd-length string of length 3 or more.

    Returns:
        The 3-character middle substring.

    Complexity:
        Time Complexity: O(1) (extracts exactly 3 characters).
        Space Complexity: O(1)

    Examples:
        >>> middle_three("Candy")
        'and'
        >>> middle_three("and")
        'and'
        >>> middle_three("solving")
        'lvi'
    """
    mid = len(s) // 2
    return s[mid - 1:mid + 2]


if __name__ == "__main__":
    print(middle_three("Candy"))
    print(middle_three("and"))
    print(middle_three("solving"))