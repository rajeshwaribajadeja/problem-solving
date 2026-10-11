"""String-1: first_two problem solution."""


def first_two(s: str) -> str:
    """Return the first two characters of a string.

    Given a string, return the string made of its first two chars, so the
    String "Hello" yields "He". If the string is shorter than length 2,
    return whatever there is.

    Args:
        s: The input string.

    Returns:
        The first two characters of the string.

    Complexity:
        Time Complexity: O(1) (slices at most 2 characters).
        Space Complexity: O(1) (output string is at most length 2).

    Examples:
        >>> first_two('Hello')
        'He'
        >>> first_two('abcdefg')
        'ab'
        >>> first_two('ab')
        'ab'
    """
    return s[:2]


if __name__ == "__main__":
    print(first_two("Hello"))
    print(first_two("abcdefg"))
    print(first_two("ab"))
