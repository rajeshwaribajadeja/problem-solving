"""Warmup-2: countxx problem solution."""


def countxx(s: str) -> int:
    """Return the count of 'xx' in string s, allowing overlap.

    Args:
        s: Input string.

    Returns:
        Number of overlapping 'xx' occurrences in s.

    Complexity:
        Time Complexity: O(n) where n is the length of s.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> countxx("abcxx")
        1
        >>> countxx("xxx")
        2
        >>> countxx("xxxx")
        3
    """
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] == "x":
            count += 1
    return count


if __name__ == "__main__":
    print(countxx("abcxx"))
    print(countxx("xxx"))
    print(countxx("xxxx"))