"""Functional-2: no_yy problem solution."""


def no_yy(words: list) -> list:
    """Return a list where each string has 'y' appended, omitting any
    with 'yy'.

    Args:
        words: List of strings.

    Returns:
        List of strings with 'y' appended, omitting any that contain 'yy'.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> no_yy(["a", "b", "c"])
        ['ay', 'by', 'cy']
        >>> no_yy(["a", "b", "cy"])
        ['ay', 'by']
        >>> no_yy(["xx", "ya", "zz"])
        ['xxy', 'yay', 'zzy']
    """

    words = list(map(lambda x: x + "y", words))

    return list(filter(lambda x: "yy" not in x, words))


if __name__ == "__main__":
    print(no_yy(["a", "b", "c"]))
    print(no_yy(["a", "b", "cy"]))
    print(no_yy(["xx", "ya", "zz"]))
