"""Recursion-1: count_abc problem solution."""


def count_abc(s: str) -> int:
    """Return recursively the count of 'abc' and 'aba' substrings in s.

    Args:
        s: Input string.

    Returns:
        Total occurrences of 'abc' and 'aba'.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> count_abc("abc")
        1
        >>> count_abc("abcxxabc")
        2
        >>> count_abc("abaxxaba")
        2
    """

    return 0 if len(s) < 3 else 1 + count_abc(s[1:]) if s[0:3] == "abc" or s[0:3] == "aba" else count_abc(s[1:]) 


if __name__ == "__main__":
    print(count_abc("abc"))
    print(count_abc("abcxxabc"))
    print(count_abc("abaxxaba"))
