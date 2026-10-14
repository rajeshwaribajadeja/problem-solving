"""Functional-2: no_long problem solution."""


def no_long(words: list) -> list:
    """Return a list of strings omitting any of length 4 or more.

    Args:
        words: List of strings.

    Returns:
        List of strings whose lengths are strictly less than 4.

    Complexity:
        Time Complexity: O(n) where n is the number of words.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> no_long(["this", "not", "too", "long"])
        ['not', 'too']
        >>> no_long(["a", "bbb", "cccc"])
        ['a', 'bbb']
        >>> no_long(["cccc", "cccc", "cccc"])
        []
    """

    return list(filter(lambda x: len(x) < 4, words))


if __name__ == "__main__":
    print(no_long(["this", "not", "too", "long"]))
    print(no_long(["a", "bbb", "cccc"]))
    print(no_long(["cccc", "cccc", "cccc"]))
