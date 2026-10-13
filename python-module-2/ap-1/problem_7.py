"""AP-1: words_without_list problem solution."""


def words_without_list(words: list, length: int) -> list:
    """Return a new list omitting all strings of the given length.

    Args:
        words: A list of strings.
        length: Length of strings to omit.

    Returns:
        A list of strings with length != length.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> words_without_list(["a", "bb", "b", "ccc"], 1)
        ['bb', 'ccc']
        >>> words_without_list(["a", "bb", "b", "ccc"], 3)
        ['a', 'bb', 'b']
        >>> words_without_list(["a", "bb", "b", "ccc"], 4)
        ['a', 'bb', 'b', 'ccc']
    """
    return [word for word in words if len(word) != length]


if __name__ == "__main__":
    print(words_without_list(["a", "bb", "b", "ccc"], 1))
    print(words_without_list(["a", "bb", "b", "ccc"], 3))
    print(words_without_list(["a", "bb", "b", "ccc"], 4))