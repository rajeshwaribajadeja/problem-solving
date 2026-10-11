"""String-1: left2 problem solution."""


def left2(s: str) -> str:
    """Return a 'rotated left 2' version where the first 2 chars move to the end.

    Given a string, return a "rotated left 2" version where the first 2
    chars are moved to the end. The string length will be at least 2.

    Args:
        s: An input string of length 2 or more.

    Returns:
        The string rotated left by 2 positions.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the rotated string.

    Examples:
        >>> left2('Hello')
        'lloHe'
        >>> left2('java')
        'vaja'
        >>> left2('Hi')
        'Hi'
    """
    return s[2:] + s[:2]


if __name__ == "__main__":
    print(left2("Hello"))
    print(left2("java"))
    print(left2("Hi"))
