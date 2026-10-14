"""Map-2: word_append problem solution."""


def word_append(words: list) -> str:
    """Append a string to result every 2nd, 4th, 6th, etc. time it appears.

    Args:
        words: List of strings.

    Returns:
        String composed of words appended upon their even appearances.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the frequency map and result string.

    Examples:
        >>> word_append(["a", "b", "a"])
        'a'
        >>> word_append(["a", "b", "a", "c", "a", "d", "a"])
        'aa'
        >>> word_append(["a", "", "a"])
        'a'
    """
    counts = {}
    result = []
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        if counts[word] % 2 == 0:
            result.append(word)
    return "".join(result)


if __name__ == "__main__":
    print(word_append(["a", "b", "a"]))
    print(word_append(["a", "b", "a", "c", "a", "d", "a"]))
    print(word_append(["a", "", "a"]))