"""Map-2: first_char problem solution."""


def first_char(words: list) -> dict:
    """Return dictionary mapping first chars to all strings starting with
    them.

    Args:
        words: List of non-empty strings.

    Returns:
        Dictionary mapping each first character to the concatenated strings
        starting with that character.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the resulting dictionary and strings.

    Examples:
        >>> first_char(["salt", "tea", "soda", "toast"])
        {'s': 'saltsoda', 't': 'teatoast'}
        >>> first_char(["aa", "bb", "cc", "aAA", "cCC", "d"])
        {'a': 'aaaAA', 'b': 'bb', 'c': 'cccCC', 'd': 'd'}
        >>> first_char([])
        {}
    """
    result = {}
    for word in words:
        key = word[0]
        result[key] = result.get(key, "") + word
    return result


if __name__ == "__main__":
    print(first_char(["salt", "tea", "soda", "toast"]))
    print(first_char(["aa", "bb", "cc", "aAA", "cCC", "d"]))
    print(first_char([]))