"""Functional-2: no_34 problem solution."""


def no_34(words: list) -> list:
    """Return a list of strings omitting any of length 3 or 4.

    Args:
        words: List of strings.

    Returns:
        List of strings whose lengths are neither 3 nor 4.

    Complexity:
        Time Complexity: O(n) where n is the number of words.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> no_34(["a", "bb", "ccc"])
        ['a', 'bb']
        >>> no_34(["a", "bb", "ccc", "dddd"])
        ['a', 'bb']
        >>> no_34(["ccc", "dddd", "apple"])
        ['apple']
    """

    return list(filter(lambda x: len(x) != 3 and len(x) != 4, words))


if __name__ == "__main__":
    print(no_34(["a", "bb", "ccc"]))
    print(no_34(["a", "bb", "ccc", "dddd"]))
    print(no_34(["ccc", "dddd", "apple"]))
