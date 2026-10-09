"""Warmup-1: front3 problem solution."""


def front3(s: str) -> str:
    """Create a new string made of 3 copies of the first 3 characters.

    Given a string, the front is defined as the first 3 characters of the
    string. If the string length is less than 3, whatever characters are
    present are used. Return a new string made of 3 copies of the front.

    Args:
        s: The input string.

    Returns:
        A string made of 3 copies of the front characters.

    Complexity:
        Time Complexity: O(1) (slices at most 3 chars and repeats 3 times).
        Space Complexity: O(1) (resulting string length is at most 9 chars).

    Examples:
        >>> front3('Java')
        'JavJavJav'
        >>> front3('Chocolate')
        'ChoChoCho'
        >>> front3('abc')
        'abcabcabc'
    """
    return s[:3] * 3


if __name__ == "__main__":
    print(front3("Java"))
    print(front3("Chocolate"))
    print(front3("abc"))