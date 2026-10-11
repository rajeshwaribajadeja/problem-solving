"""String-1: withouend2 problem solution."""


def withouend2(s: str) -> str:
    """Return a version without both the first and last char of the string.

    Given a string, return a version without both the first and last
    char of the string. The string may be any length, including 0.

    Args:
        s: The input string.

    Returns:
        The string with the first and last characters omitted.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the trimmed string.

    Examples:
        >>> withouend2("Hello")
        'ell'
        >>> withouend2("abc")
        'b'
        >>> withouend2("ab")
        ''
    """
    return s[1:-1]


if __name__ == "__main__":
    print(withouend2("Hello"))
    print(withouend2("abc"))
    print(withouend2("ab"))