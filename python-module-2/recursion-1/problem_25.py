"""Recursion-1: count_hi_2 problem solution."""


def count_hi_2(s: str) -> int:
    """Return count of 'hi' in s, ignoring any 'hi' preceded by 'x'.

    Args:
        s: Input string.

    Returns:
        Number of valid 'hi' substrings.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> count_hi_2("ahixhi")
        1
        >>> count_hi_2("ahibhi")
        2
        >>> count_hi_2("xhixhi")
        0
    """
    if len(s) < 2:
        return 0
    if len(s) >= 3 and s[0] == "x" and s[1:3] == "hi":
        return count_hi_2(s[3:])
    if s[:2] == "hi":
        return 1 + count_hi_2(s[2:])
    return count_hi_2(s[1:])


if __name__ == "__main__":
    print(count_hi_2("ahixhi"))
    print(count_hi_2("ahibhi"))
    print(count_hi_2("xhixhi"))
