"""Recursion-1: end_x problem solution."""


def end_x(s: str) -> str:
    """Return a new string where all lowercase 'x' are moved to the end.

    Args:
        s: Input string.

    Returns:
        String with all 'x' characters placed at the end.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> end_x("xxre")
        'rexx'
        >>> end_x("xxhixx")
        'hixxxx'
        >>> end_x("xhixhix")
        'hihixxx'
    """

    return "" if not s else (end_x(s[1:]) + "x" if s[0] == "x" else s[0] + end_x(s[1:]))


if __name__ == "__main__":
    print(end_x("xxre"))
    print(end_x("xxhixx"))
    print(end_x("xhixhix"))
