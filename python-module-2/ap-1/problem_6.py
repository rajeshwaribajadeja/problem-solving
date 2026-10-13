"""AP-1: words_front problem solution."""


def words_front(words: list, n: int) -> list:
    """Return a new array containing the first n strings.

    Given an array of strings, return a new array containing the first
    n strings. n will be in the range 1..length.

    Args:
        words: A list of strings.
        n: Number of strings to include (1 <= n <= len(words)).

    Returns:
        A list of the first n strings.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)

    Examples:
        >>> words_front(["a", "b", "c", "d"], 1)
        ['a']
        >>> words_front(["a", "b", "c", "d"], 2)
        ['a', 'b']
        >>> words_front(["a", "b", "c", "d"], 3)
        ['a', 'b', 'c']
    """
    return words[:n]


if __name__ == "__main__":
    print(words_front(["a", "b", "c", "d"], 1))
    print(words_front(["a", "b", "c", "d"], 2))
    print(words_front(["a", "b", "c", "d"], 3))