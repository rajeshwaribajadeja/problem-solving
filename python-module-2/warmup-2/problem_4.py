"""Warmup-2: altpairs problem solution."""


def altpairs(s: str) -> str:
    """Return a string made of the chars at indexes 0,1, 4,5, 8,9, etc.

    Args:
        s: Input string.

    Returns:
        String composed of alternating index pairs.

    Complexity:
        Time Complexity: O(n) where n is the length of s.
        Space Complexity: O(n) for the newly constructed string.

    Examples:
        >>> altpairs("kitten")
        'kien'
        >>> altpairs("Chocolate")
        'Chole'
        >>> altpairs("CodingHorror")
        'Congrr'
    """
    return "".join(s[i:i + 2] for i in range(0, len(s), 4))


if __name__ == "__main__":
    print(altpairs("kitten"))
    print(altpairs("Chocolate"))
    print(altpairs("CodingHorror"))