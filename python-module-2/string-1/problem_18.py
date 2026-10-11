"""String-1: without2 problem solution."""


def without2(s: str) -> str:
    """Omit length 2 substring from beginning if it appears at both ends.

    Given a string, if a length 2 substring appears at both its beginning
    and end, return a string without the substring at the beginning, so
    "HelloHe" yields "lloHe". The substring may overlap with itself, so
    "Hi" yields "". Otherwise, return the original string unchanged.

    Args:
        s: The input string.

    Returns:
        The string with the front 2 characters removed if matching end, else s.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the result.

    Examples:
        >>> without2("HelloHe")
        'lloHe'
        >>> without2("HelloHi")
        'HelloHi'
        >>> without2("Hi")
        ''
    """
    return s[2:] if s[:2] == s[-2:] else s

if __name__ == "__main__":
    print(without2("HelloHe"))
    print(without2("HelloHi"))
    print(without2("Hi"))