"""String-1: extra_front problem solution."""


def extra_front(s: str) -> str:
    """Return a new string made of 3 copies of the first 2 characters.

    Given a string, return a new string made of 3 copies of the first 2
    chars of the original string. The string may be any length. If there
    are fewer than 2 chars, use whatever is there.

    Args:
        s: The input string.

    Returns:
        A string of 3 copies of the front characters.

    Complexity:
        Time Complexity: O(1) (slices at most 2 characters and repeats 3 times).
        Space Complexity: O(1) (result length <= 6).

    Examples:
        >>> extra_front("Hello")
        'HeHeHe'
        >>> extra_front("ab")
        'ababab'
        >>> extra_front("H")
        'HHH'
    """
    return s[:2] * 3


if __name__ == "__main__":
    print(extra_front("Hello"))
    print(extra_front("ab"))
    print(extra_front("H"))