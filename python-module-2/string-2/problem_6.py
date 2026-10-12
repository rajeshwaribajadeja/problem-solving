"""String-2: repeat_separator problem solution."""


def repeat_separator(word: str, sep: str, count: int) -> str:
    """Return count occurrences of word, separated by sep.

    Given two strings, word and a separator sep, return a big string
    made of count occurrences of the word, separated by the separator
    string.

    Args:
        word: The word string.
        sep: The separator string.
        count: The number of occurrences of word.

    Returns:
        The concatenated repeated-separator string.

    Complexity:
        Time Complexity: O(count * (len(word) + len(sep))).
        Space Complexity: O(count * (len(word) + len(sep))) to store the result.

    Examples:
        >>> repeat_separator("Word", "X", 3)
        'WordXWordXWord'
        >>> repeat_separator("This", "And", 2)
        'ThisAndThis'
        >>> repeat_separator("This", "And", 1)
        'This'
    """
    return sep.join([word] * count) if count > 0 else ""


if __name__ == "__main__":
    print(repeat_separator("Word", "X", 3))
    print(repeat_separator("This", "And", 2))
    print(repeat_separator("This", "And", 1))