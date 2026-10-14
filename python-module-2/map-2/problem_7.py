"""Map-2: word_multiple problem solution."""


def word_multiple(words: list) -> dict:
    """Return dictionary mapping each string to True if it appears >= 2 times.

    Args:
        words: List of strings.

    Returns:
        Dictionary mapping each string to True if it appears 2 or more
        times, or False otherwise.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the resulting dictionary.

    Examples:
        >>> word_multiple(["a", "b", "a", "c", "b"])
        {'a': True, 'b': True, 'c': False}
        >>> word_multiple(["c", "b", "a"])
        {'c': False, 'b': False, 'a': False}
        >>> word_multiple(["c", "c", "c", "c"])
        {'c': True}
    """
    result = {}
    for word in words:
        if word in result:
            result[word] = True
        else:
            result[word] = False
    return result


if __name__ == "__main__":
    print(word_multiple(["a", "b", "a", "c", "b"]))
    print(word_multiple(["c", "b", "a"]))
    print(word_multiple(["c", "c", "c", "c"]))