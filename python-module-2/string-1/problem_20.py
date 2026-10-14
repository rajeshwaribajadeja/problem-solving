"""String-1: start_word problem solution."""


def start_word(s: str, word: str) -> str:
    """Return the front of s matching word, ignoring the first character.

    Given a string and a second "word" string, we'll say that the word
    matches the string if it appears at the front of the string, except
    its first char does not need to match exactly. On a match, return the
    front of the string, or otherwise return the empty string.

    Args:
        s: The input string.
        word: The match pattern string of length at least 1.

    Returns:
        The matched prefix from s, or an empty string.

    Complexity:
        Time Complexity: O(len(word)).
        Space Complexity: O(len(word)) to store the sliced output.

    Examples:
        >>> start_word("hippo", "hi")
        'hi'
        >>> start_word("hippo", "xip")
        'hip'
        >>> start_word("hippo", "i")
        'h'
    """
    return (
        s[:len(word)]
        if len(s) >= len(word) and s[1:len(word)] == word[1:]
        else ""
    )


if __name__ == "__main__":
    print(start_word("hippo", "hi"))
    print(start_word("hippo", "xip"))
    print(start_word("hippo", "i"))