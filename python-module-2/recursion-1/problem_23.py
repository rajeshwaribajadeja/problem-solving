"""Recursion-1: count_11 problem solution."""


def count_11(s: str) -> int:
    """Return count of non-overlapping '11' substrings in s.

    Args:
        s: Input string.

    Returns:
        Number of non-overlapping '11' occurrences.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> count_11("11abc11")
        2
        >>> count_11("abc11x11x11")
        3
        >>> count_11("111")
        1
    """
    return (
        0 if len(s) < 2
        else 1 + count_11(s[2:]) if s[:2] == "11"
        else count_11(s[1:])
    )


if __name__ == "__main__":
    print(count_11("11abc11"))
    print(count_11("abc11x11x11"))
    print(count_11("111"))
