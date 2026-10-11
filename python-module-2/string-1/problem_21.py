"""String-1: without_x problem solution."""


def without_x(s: str) -> str:
    """Return string without 'x' if the first or last characters are 'x'.

    Given a string, if the first or last chars are 'x', return the
    string without those 'x' chars, and otherwise return the string
    unchanged.

    Args:
        s: The input string.

    Returns:
        The string with leading and trailing 'x' removed if present.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the modified string.

    Examples:
        >>> without_x("xHix")
        'Hi'
        >>> without_x("xHi")
        'Hi'
        >>> without_x("Hxix")
        'Hxi'
    """
    return s[s.startswith("x"):len(s) - s.endswith("x")]


if __name__ == "__main__":
    print(without_x("xHix"))
    print(without_x("xHi"))
    print(without_x("Hxix"))