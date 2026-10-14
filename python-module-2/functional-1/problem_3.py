"""Functional-1: add_star problem solution."""


def add_star(words: list) -> list:
    """Return a list where each string has '*' appended to its end.

    Args:
        words: List of strings.

    Returns:
        List of strings with '*' added at the end of each.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> add_star(["a", "bb", "ccc"])
        ['a*', 'bb*', 'ccc*']
        >>> add_star(["hello", "there"])
        ['hello*', 'there*']
        >>> add_star(["*"])
        ['**']
    """

    return list(map(lambda x: x + "*", words))


if __name__ == "__main__":
    print(add_star(["a", "bb", "ccc"]))
    print(add_star(["hello", "there"]))
    print(add_star(["*"]))
