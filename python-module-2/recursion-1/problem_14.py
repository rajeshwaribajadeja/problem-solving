"""Recursion-1: no_x problem solution."""


def no_x(s: str) -> str:
    """Return a new string where all lowercase 'x' chars have been removed.

    Args:
        s: Input string.

    Returns:
        String with all 'x' characters stripped.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> no_x("xaxb")
        'ab'
        >>> no_x("abc")
        'abc'
        >>> no_x("xx")
        ''
    """

    return "" if not s else no_x(s[1:]) if s[0] == "x" else s[0] + no_x(s[1:])


if __name__ == "__main__":
    print(no_x("xaxb"))
    print(no_x("abc"))
    print(no_x("xx"))
