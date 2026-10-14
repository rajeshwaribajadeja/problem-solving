"""Recursion-1: str_copies problem solution."""


def str_copies(s: str, sub: str, n: int) -> bool:
    """Return True if at least n copies of sub appear in s (may overlap).

    Args:
        s: Input string.
        sub: Non-empty substring to match.
        n: Required count of occurrences.

    Returns:
        True if at least n copies appear in s, False otherwise.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> str_copies("catcowcat", "cat", 2)
        True
        >>> str_copies("catcowcat", "cow", 2)
        False
        >>> str_copies("catcowcat", "cow", 1)
        True
    """
    if n <= 0:
        return True
    if len(s) < len(sub):
        return False
    if s[:len(sub)] == sub:
        return str_copies(s[1:], sub, n - 1)
    return str_copies(s[1:], sub, n)


if __name__ == "__main__":
    print(str_copies("catcowcat", "cat", 2))
    print(str_copies("catcowcat", "cow", 2))
    print(str_copies("catcowcat", "cow", 1))
