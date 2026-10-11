"""String-1: de_front problem solution."""


def de_front(s: str) -> str:
    """Return string omitting first 2 chars except 'a' at 0 and 'b' at 1.

    Given a string, return a version without the first 2 chars. Except
    keep the first char if it is 'a' and keep the second char if it is 'b'.
    The string may be any length.

    Args:
        s: The input string.

    Returns:
        The filtered string.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the result.

    Examples:
        >>> de_front("Hello")
        'llo'
        >>> de_front("java")
        'va'
        >>> de_front("away")
        'aay'
    """
    return s[:1] * (s[:1] == "a") + s[1:2] * (s[1:2] == "b") + s[2:]


if __name__ == "__main__":
    print(de_front("Hello"))
    print(de_front("java"))
    print(de_front("away"))