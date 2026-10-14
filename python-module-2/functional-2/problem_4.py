"""Functional-2: no_z problem solution."""


def no_z(words: list) -> list:
    """Return a list of strings omitting any that contain the letter 'z'.

    Args:
        words: List of strings.

    Returns:
        List of strings without 'z'.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> no_z(["aaa", "bbb", "aza"])
        ['aaa', 'bbb']
        >>> no_z(["hziz", "hzello", "hi"])
        ['hi']
        >>> no_z(["hello", "howz", "are", "youz"])
        ['hello', 'are']
    """

    return list(filter(lambda x: "z" not in x, words))


if __name__ == "__main__":
    print(no_z(["aaa", "bbb", "aza"]))
    print(no_z(["hziz", "hzello", "hi"]))
    print(no_z(["hello", "howz", "are", "youz"]))
