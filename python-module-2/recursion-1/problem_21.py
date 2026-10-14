"""Recursion-1: count_pairs problem solution."""


def count_pairs(s: str) -> int:
    """Return count of pairs where a char is separated by another char.

    For example, 'AxA' makes a pair. Pairs can overlap.

    Args:
        s: Input string.

    Returns:
        Number of pair occurrences.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> count_pairs("axa")
        1
        >>> count_pairs("axax")
        2
        >>> count_pairs("axbx")
        1
    """
    return 0 if len(s) < 3 else 1 + count_pairs(s[1:]) if s[0] == s[2] else count_pairs(s[1:])

if __name__ == "__main__":
    print(count_pairs("axa"))
    print(count_pairs("axax"))
    print(count_pairs("axbx"))
