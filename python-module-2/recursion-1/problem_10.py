"""Recursion-1: count_x problem solution."""


def count_x(s: str) -> int:
    """Return the count of lowercase 'x' chars in string s recursively.

    Args:
        s: Input string.

    Returns:
        Number of 'x' characters in s.

    Complexity:
        Time Complexity: O(n^2) due to slicing of length n.
        Space Complexity: O(n^2) auxiliary space for sliced substrings.

    Examples:
        >>> count_x("xxhixx")
        4
        >>> count_x("xhixhix")
        3
        >>> count_x("hi")
        0
    """

    return 0 if not s else (1 if s[0] == "x" else 0) + count_x(s[1:])


if __name__ == "__main__":
    print(count_x("xxhixx"))
    print(count_x("xhixhix"))
    print(count_x("hi"))
