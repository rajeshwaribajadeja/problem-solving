"""String-1: without_x2 problem solution."""


def without_x2(s: str) -> str:
    """Return string without 'x' if one or both of the first 2 chars is 'x'.

    Given a string, if one or both of the first 2 chars is 'x', return
    the string without those 'x' chars, and otherwise return the string
    unchanged.

    Args:
        s: The input string.

    Returns:
        The string without 'x' in the first two positions.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the result.

    Examples:
        >>> without_x2("xHi")
        'Hi'
        >>> without_x2("Hxi")
        'Hi'
        >>> without_x2("Hi")
        'Hi'
    """
    return s[:1] * (s[:1] != "x") + s[1:2] * (s[1:2] != "x") + s[2:]


if __name__ == "__main__":
    print(without_x2("xHi"))
    print(without_x2("Hxi"))
    print(without_x2("Hi"))