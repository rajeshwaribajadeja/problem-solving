"""String-1: at_first problem solution."""


def at_first(s: str) -> str:
    """Return a string of length 2 from the front, padding with '@' if needed.

    Given a string, return a string length 2 made of its first 2 chars.
    If the string length is less than 2, use '@' for the missing chars.

    Args:
        s: The input string.

    Returns:
        A 2-character string prefixed from s, padded with '@'.

    Complexity:
        Time Complexity: O(1) (output is at most 2 characters).
        Space Complexity: O(1)

    Examples:
        >>> at_first("hello")
        'he'
        >>> at_first("hi")
        'hi'
        >>> at_first("h")
        'h@'
    """
    return s + "@" * (2 - len(s)) if len(s) < 2 else s[:2]


if __name__ == "__main__":
    print(at_first("hello"))
    print(at_first("hi"))
    print(at_first("h"))