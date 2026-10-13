"""AP-1: words_count problem solution."""


def words_count(words: list, length: int) -> int:
    """Return count of strings that have the specified length.

    Given an array of strings, return the count of the number of strings
    with the given length.

    Args:
        words: A list of strings.
        length: Target word length.

    Returns:
        The number of words with len(word) == length.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> words_count(["a", "bb", "b", "ccc"], 1)
        2
        >>> words_count(["a", "bb", "b", "ccc"], 3)
        1
        >>> words_count(["a", "bb", "b", "ccc"], 4)
        0
    """
    return sum(1 for word in words if len(word) == length)


if __name__ == "__main__":
    print(words_count(["a", "bb", "b", "ccc"], 1))
    print(words_count(["a", "bb", "b", "ccc"], 3))
    print(words_count(["a", "bb", "b", "ccc"], 4))