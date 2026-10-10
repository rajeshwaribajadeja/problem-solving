"""Warmup-1: back_around problem solution."""


def back_around(s: str) -> str:
    """Return a string with the last character added at the front and back.

    Given a string, take the last char and return a new string with the
    last char added at the front and back. The original string will be
    length 1 or more.

    Args:
        s: The input string of length 1 or more.

    Returns:
        The new string with the last character at front and back.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting string of length N + 2.

    Examples:
        >>> back_around("cat")
        'tcatt'
        >>> back_around("Hello")
        'oHelloo'
        >>> back_around("a")
        'aaa'
    """
    return s[-1] + s + s[-1]


if __name__ == "__main__":
    print(back_around("cat"))
    print(back_around("Hello"))
    print(back_around("a"))