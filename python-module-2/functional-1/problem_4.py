"""Functional-1: copies_3 problem solution."""


def copies_3(words: list) -> list:
    """Return a list where each string is replaced by 3 copies of itself.

    Args:
        words: List of strings.

    Returns:
        List of strings with each original string triplicated.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> copies_3(["a", "bb", "ccc"])
        ['aaa', 'bbbbbb', 'ccccccccc']
        >>> copies_3(["24", "a", ""])
        ['242424', 'aaa', '']
        >>> copies_3(["hello", "there"])
        ['hellohellohello', 'theretherethere']
    """

    return list(map(lambda x: x * 3, words))


if __name__ == "__main__":
    print(copies_3(["a", "bb", "ccc"]))
    print(copies_3(["24", "a", ""]))
    print(copies_3(["hello", "there"]))
