"""Recursion-1: count_hi problem solution."""


def count_hi(s: str) -> int:
    """Return the count of lowercase 'hi' occurrences in string s.

    Args:
        s: Input string.

    Returns:
        Number of times 'hi' appears in s.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> count_hi("xxhixx")
        1
        >>> count_hi("xhixhix")
        2
        >>> count_hi("hi")
        1
    """
    if len(s) < 2:
        return 0
    if s[:2] == "hi":
        return 1 + count_hi(s[2:])
    return count_hi(s[1:])


if __name__ == "__main__":
    print(count_hi("xxhixx"))
    print(count_hi("xhixhix"))
    print(count_hi("hi"))
