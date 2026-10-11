"""String-1: first_half problem solution."""


def first_half(s: str) -> str:
    """Return the first half of an even-length string.

    Given a string of even length, return the first half. So the string
    "WooHoo" yields "Woo".

    Args:
        s: An even-length input string.

    Returns:
        The first half of the string.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the half-length string.

    Examples:
        >>> first_half('WooHoo')
        'Woo'
        >>> first_half('HelloThere')
        'Hello'
        >>> first_half('abcdef')
        'abc'
    """
    return s[:len(s) // 2]


if __name__ == "__main__":
    print(first_half("WooHoo"))
    print(first_half("HelloThere"))
    print(first_half("abcdef"))
