"""Map-2: word_0 problem solution."""


def word_0(words: list) -> dict:
    """Return a dictionary with a key for every string, with value 0.

    Args:
        words: List of strings.

    Returns:
        Dictionary mapping each unique string to 0.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created dictionary.

    Examples:
        >>> word_0(["a", "b", "a", "b"])
        {'a': 0, 'b': 0}
        >>> word_0(["a", "b", "a", "c", "b"])
        {'a': 0, 'b': 0, 'c': 0}
        >>> word_0(["c", "b", "a"])
        {'c': 0, 'b': 0, 'a': 0}
    """
    result = {}
    for word in words:
        result[word] = 0
    return result


if __name__ == "__main__":
    print(word_0(["a", "b", "a", "b"]))
    print(word_0(["a", "b", "a", "c", "b"]))
    print(word_0(["c", "b", "a"]))