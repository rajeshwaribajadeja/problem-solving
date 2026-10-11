"""String-1: two_char problem solution."""


def two_char(s: str, i: int) -> str:
    """Return a string of length 2 starting at index i, or front 2 on invalid index.

    Given a string and an index, return a string length 2 starting at
    the given index. If the index is too big or too small to define a
    string length 2, use the first 2 chars. The string length will be at
    least 2.

    Args:
        s: An input string of length at least 2.
        i: The starting index.

    Returns:
        A 2-character substring starting at index i or at index 0.

    Complexity:
        Time Complexity: O(1) (slices at most 2 characters).
        Space Complexity: O(1)

    Examples:
        >>> two_char("java", 0)
        'ja'
        >>> two_char("java", 2)
        'va'
        >>> two_char("java", 3)
        'ja'
    """
    return s[i:i+2] if 0 <= i < len(s)-1 else s[:2]

if __name__ == "__main__":
    print(two_char("java", 0))
    print(two_char("java", 2))
    print(two_char("java", 3))