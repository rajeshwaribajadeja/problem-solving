"""AP-1: words_without problem solution."""


def words_without(words: list, target: str) -> list:
    """Return a new array without strings equal to the target string.

    Given an array of strings, return a new array without the strings
    that are equal to the target string.

    Args:
        words: A list of strings.
        target: The target string to exclude.

    Returns:
        A list of strings not equal to target.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space for the result.

    Examples:
        >>> words_without(["a", "b", "c", "a"], "a")
        ['b', 'c']
        >>> words_without(["a", "b", "c", "a"], "b")
        ['a', 'c', 'a']
        >>> words_without(["a", "b", "c", "a"], "c")
        ['a', 'b', 'a']
    """
    return [word for word in words if word != target]


if __name__ == "__main__":
    print(words_without(["a", "b", "c", "a"], "a"))
    print(words_without(["a", "b", "c", "a"], "b"))
    print(words_without(["a", "b", "c", "a"], "c"))