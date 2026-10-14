"""Functional-1: no_x problem solution."""


def no_x(words: list) -> list:
    """Return a list where each string has all 'x' characters removed.

    Args:
        words: List of strings.

    Returns:
        List of strings with all 'x' characters stripped.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> no_x(["ax", "bb", "cx"])
        ['a', 'bb', 'c']
        >>> no_x(["xxax", "xbxbx", "xxcx"])
        ['a', 'bb', 'c']
        >>> no_x(["x"])
        ['']
    """

    return list(map(lambda x: x.replace("x", ""), words))


if __name__ == "__main__":
    print(no_x(["ax", "bb", "cx"]))
    print(no_x(["xxax", "xbxbx", "xxcx"]))
    print(no_x(["x"]))
