"""Warmup-1: missing_char problem solution."""


def missing_char(s: str, n: int) -> str:
    """Return a new string where the character at index n has been removed.

    Given a non-empty string and an int n, return a new string where the
    char at index n has been removed. The value of n will be a valid index
    in the original string (0 <= n < len(s)).

    Args:
        s: The non-empty input string.
        n: The 0-based index of the character to remove.

    Returns:
        A new string with the character at index n omitted.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting sliced string.

    Examples:
        >>> missing_char('kitten', 1)
        'ktten'
        >>> missing_char('kitten', 0)
        'itten'
        >>> missing_char('kitten', 4)
        'kittn'
    """
    return s[:n] + s[n + 1:]


if __name__ == "__main__":
    print(missing_char("kitten", 1))
    print(missing_char("kitten", 0))
    print(missing_char("kitten", 4))