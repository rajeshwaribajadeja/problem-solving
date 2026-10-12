"""String-2: word_ends problem solution."""


def word_ends(s: str, word: str) -> str:
    """Return chars immediately before and after every appearance of word.

    Given a string and a non-empty word string, return a string made of
    each char just before and just after every appearance of the word in
    the string.

    Args:
        s: The input string.
        word: The non-empty target word string.

    Returns:
        The concatenated characters bordering each appearance of word.

    Complexity:
        Time Complexity: O(len(s) * len(word)).
        Space Complexity: O(len(s)) to store the result.

    Examples:
        >>> word_ends("abcXY123XYijk", "XY")
        'c13i'
        >>> word_ends("XY123XY", "XY")
        '13'
        >>> word_ends("XY1XY", "XY")
        '11'
    """
    result = []
    w_len = len(word)
    for i in range(len(s) - w_len + 1):
        if s[i:i + w_len] == word:
            if i > 0:
                result.append(s[i - 1])
            if i + w_len < len(s):
                result.append(s[i + w_len])
    return "".join(result)


if __name__ == "__main__":
    print(word_ends("abcXY123XYijk", "XY"))
    print(word_ends("XY123XY", "XY"))
    print(word_ends("XY1XY", "XY"))
