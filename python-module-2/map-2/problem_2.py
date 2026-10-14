"""Map-2: word_len problem solution."""


def word_len(words: list) -> dict:
    """Return a dictionary mapping each unique string to its length.

    Args:
        words: List of strings.

    Returns:
        Dictionary with each string as key and its length as value.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created dictionary.

    Examples:
        >>> word_len(["a", "bb", "a", "bb"])
        {'a': 1, 'bb': 2}
        >>> word_len(["this", "and", "that", "and"])
        {'this': 4, 'and': 3, 'that': 4}
        >>> word_len(["code", "code", "code", "bug"])
        {'code': 4, 'bug': 3}
    """
    result = {}
    for word in words:
        result[word] = len(word)
    return result


if __name__ == "__main__":
    print(word_len(["a", "bb", "a", "bb"]))
    print(word_len(["this", "and", "that", "and"]))
    print(word_len(["code", "code", "code", "bug"]))