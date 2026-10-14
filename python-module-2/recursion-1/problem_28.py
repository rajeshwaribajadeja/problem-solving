"""Recursion-1: str_count problem solution."""


def str_count(s: str, sub: str) -> int:
    """Return count of non-overlapping occurrences of sub in s.

    Args:
        s: Input string.
        sub: Non-empty substring to count.

    Returns:
        Number of non-overlapping occurrences of sub.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> str_count("catcowcat", "cat")
        2
        >>> str_count("catcowcat", "cow")
        1
        >>> str_count("catcowcat", "dog")
        0
    """
    if len(s) < len(sub):
        return 0
    if s[:len(sub)] == sub:
        return 1 + str_count(s[len(sub):], sub)
    return str_count(s[1:], sub)


if __name__ == "__main__":
    print(str_count("catcowcat", "cat"))
    print(str_count("catcowcat", "cow"))
    print(str_count("catcowcat", "dog"))
