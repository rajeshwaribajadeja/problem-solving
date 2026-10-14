"""Warmup-2: stringx problem solution."""


def stringx(s: str) -> str:
    """Return a string where all 'x' are removed except at the start and end.

    Args:
        s: Input string.

    Returns:
        String with interior 'x' characters removed.

    Complexity:
        Time Complexity: O(n) where n is the length of s.
        Space Complexity: O(n) for the newly constructed string.

    Examples:
        >>> stringx("xxHxix")
        'xHix'
        >>> stringx("abxxxcd")
        'abcd'
        >>> stringx("xabxxxcdx")
        'xabcdx'
    """
    return s if len(s) <= 2 else s[0] + s[1:-1].replace("x", "") + s[-1]


if __name__ == "__main__":
    print(stringx("xxHxix"))
    print(stringx("abxxxcd"))
    print(stringx("xabxxxcdx"))