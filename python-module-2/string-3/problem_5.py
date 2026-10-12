"""String-3: count_triple problem solution."""


def count_triple(s: str) -> int:
    """Return the number of triples in the given string (may overlap).

    We'll say that a "triple" in a string is a char appearing three
    times in a row. Return the number of triples in the given string.
    The triples may overlap.

    Args:
        s: The input string.

    Returns:
        The count of 3 identical adjacent characters.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> count_triple("abcXXXabc")
        1
        >>> count_triple("xxxabyyyycd")
        3
        >>> count_triple("a")
        0
    """
    return sum(1 for i in range(len(s) - 2) if s[i] == s[i + 1] == s[i + 2])


if __name__ == "__main__":
    print(count_triple("abcXXXabc"))
    print(count_triple("xxxabyyyycd"))
    print(count_triple("a"))