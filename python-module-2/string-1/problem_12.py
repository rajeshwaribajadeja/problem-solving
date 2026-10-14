"""String-1: concat problem solution."""


def concat(a: str, b: str) -> str:
    """Concatenate two strings, omitting double characters at the boundary.

    Given two strings, append them together (known as "concatenation")
    and return the result. However, if the concatenation creates a
    double-char, then omit one of the chars, so "abc" and "cat" yields
    "abcat".

    Args:
        a: First string.
        b: Second string.

    Returns:
        The concatenated string without double boundary characters.

    Complexity:
        Time Complexity: O(len(a) + len(b)).
        Space Complexity: O(len(a) + len(b)) to store the result.

    Examples:
        >>> concat("abc", "cat")
        'abcat'
        >>> concat("dog", "cat")
        'dogcat'
        >>> concat("abc", "")
        'abc'
    """
    return a + b[1:] if a and b and a[-1] == b[0] else a + b


if __name__ == "__main__":
    print(concat("abc", "cat"))
    print(concat("dog", "cat"))
    print(concat("abc", ""))