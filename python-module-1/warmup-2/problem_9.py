"""Warmup-2: string_match problem solution."""


def string_match(a: str, b: str) -> int:
    """Return the number of positions where two strings share the same length 2 substring.

    Given 2 strings, a and b, return the number of the positions where
    they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
    yields 3, since the "xx", "aa", and "az" substrings appear in the
    same place in both strings.

    Args:
        a: First input string.
        b: Second input string.

    Returns:
        The count of shared length-2 substring matches at the same positions.

    Complexity:
        Time Complexity: O(min(len(a), len(b))).
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> string_match('xxcaazz', 'xxbaaz')
        3
        >>> string_match('abc', 'abc')
        2
        >>> string_match('abc', 'axc')
        0
    """
    return sum(a[i:i+2] == b[i:i+2] for i in range(min(len(a), len(b)) - 1))


if __name__ == "__main__":
    print(string_match("xxcaazz", "xxbaaz"))
    print(string_match("abc", "abc"))
    print(string_match("abc", "axc"))
