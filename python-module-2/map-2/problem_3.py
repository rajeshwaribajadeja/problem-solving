"""Map-2: pairs problem solution."""


def pairs(words: list) -> dict:
    """Return dictionary mapping first char to last char of each string.

    Args:
        words: List of non-empty strings.

    Returns:
        Dictionary mapping the first character of each string to its last
        character.

    Complexity:
        Time Complexity: O(n) where n is the number of words.
        Space Complexity: O(n) for the newly created dictionary.

    Examples:
        >>> pairs(["code", "bug"])
        {'c': 'e', 'b': 'g'}
        >>> pairs(["man", "moon", "main"])
        {'m': 'n'}
        >>> pairs(["man", "moon", "good", "night"])
        {'m': 'n', 'g': 'd', 'n': 't'}
    """
    result = {}
    for word in words:
        result[word[0]] = word[-1]
    return result


if __name__ == "__main__":
    print(pairs(["code", "bug"]))
    print(pairs(["man", "moon", "main"]))
    print(pairs(["man", "moon", "good", "night"]))