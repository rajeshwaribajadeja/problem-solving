"""String-1: theend problem solution."""


def theend(s: str, front: bool) -> str:
    """Return the first char if front is True, or the last char if False.

    Given a string, return a string length 1 from its front, unless front
    is False, in which case return a string length 1 from its back.
    The string will be non-empty.

    Args:
        s: A non-empty input string.
        front: True for first char, False for last char.

    Returns:
        A string of length 1 from front or back.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> theend("Hello", True)
        'H'
        >>> theend("Hello", False)
        'o'
        >>> theend("oh", True)
        'o'
    """
    return s[0] if front else s[-1]


if __name__ == "__main__":
    print(theend("Hello", True))
    print(theend("Hello", False))
    print(theend("oh", True))