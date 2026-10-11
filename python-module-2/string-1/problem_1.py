"""String-1: right2 problem solution."""


def right2(s: str) -> str:
    """Return a 'rotated right 2' version where the last 2 chars move to start.

    Given a string, return a "rotated right 2" version where the last 2
    chars are moved to the start. The string length will be at least 2.

    Args:
        s: An input string of length 2 or more.

    Returns:
        The string rotated right by 2 characters.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the rotated string.

    Examples:
        >>> right2("Hello")
        'loHel'
        >>> right2("java")
        'vaja'
        >>> right2("Hi")
        'Hi'
    """
    return s[-2:] + s[:-2]


if __name__ == "__main__":
    print(right2("Hello"))
    print(right2("java"))
    print(right2("Hi"))