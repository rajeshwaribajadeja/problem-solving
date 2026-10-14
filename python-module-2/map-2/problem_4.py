"""Map-2: word_count problem solution."""


def word_count(words: list) -> dict:
    """Return a dictionary counting occurrences of each string in words.

    Args:
        words: List of strings.

    Returns:
        Dictionary mapping each unique string to its frequency count.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the frequency dictionary.

    Examples:
        >>> word_count(["a", "b", "a", "c", "b"])
        {'a': 2, 'b': 2, 'c': 1}
        >>> word_count(["c", "b", "a"])
        {'c': 1, 'b': 1, 'a': 1}
        >>> word_count(["c", "c", "c", "c"])
        {'c': 4}
    """
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result


if __name__ == "__main__":
    print(word_count(["a", "b", "a", "c", "b"]))
    print(word_count(["c", "b", "a"]))
    print(word_count(["c", "c", "c", "c"]))