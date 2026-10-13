"""Logic-1: cigar_party problem solution."""


def cigar_party(cigars: int, is_weekend: bool) -> bool:
    """Return True if the squirrel cigar party is successful.

    A squirrel party is successful when the number of cigars is between
    40 and 60, inclusive, unless it is the weekend, in which case there
    is no upper bound.

    Args:
        cigars: Number of cigars.
        is_weekend: Whether it is the weekend.

    Returns:
        True if the party is successful, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> cigar_party(30, False)
        False
        >>> cigar_party(50, False)
        True
        >>> cigar_party(70, True)
        True
    """
    return 40 <= cigars <= 60 if not is_weekend else cigars >= 40


if __name__ == "__main__":
    print(cigar_party(30, False))
    print(cigar_party(50, False))
    print(cigar_party(70, True))