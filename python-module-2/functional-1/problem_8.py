"""Functional-1: lower problem solution."""


def lower(words: list) -> list:
    """Return a list where each string is converted to lowercase.

    Args:
        words: List of strings.

    Returns:
        List of strings in lowercase.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> lower(["Hello", "Hi"])
        ['hello', 'hi']
        >>> lower(["AAA", "BBB", "ccc"])
        ['aaa', 'bbb', 'ccc']
        >>> lower(["KitteN", "ChocolaTE"])
        ['kitten', 'chocolate']
    """

    return list(map(lambda x: x.lower(), words))


if __name__ == "__main__":
    print(lower(["Hello", "Hi"]))
    print(lower(["AAA", "BBB", "ccc"]))
    print(lower(["KitteN", "ChocolaTE"]))
