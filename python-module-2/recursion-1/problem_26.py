"""Recursion-1: paren_bit problem solution."""


def paren_bit(s: str) -> str:
    """Return substring containing parenthesis and their contents.

    Args:
        s: Input string containing a single pair of parentheses.

    Returns:
        The parenthesized substring including parentheses.

    Complexity:
        Time Complexity: O(n^2) due to recursive slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> paren_bit("xyz(abc)123")
        '(abc)'
        >>> paren_bit("x(hello)")
        '(hello)'
        >>> paren_bit("(xy)1")
        '(xy)'
    """
    if s[0] != "(":
        return paren_bit(s[1:])
    if s[-1] != ")":
        return paren_bit(s[:-1])
    return s


if __name__ == "__main__":
    print(paren_bit("xyz(abc)123"))
    print(paren_bit("x(hello)"))
    print(paren_bit("(xy)1"))
