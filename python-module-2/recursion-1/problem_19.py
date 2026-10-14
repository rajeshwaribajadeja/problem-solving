"""Recursion-1: pair_star problem solution."""


def pair_star(s: str) -> str:
    """Return string where identical adjacent chars are separated by '*'.

    Args:
        s: Input string.

    Returns:
        String with identical adjacent characters separated by '*'.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> pair_star("hello")
        'hel*lo'
        >>> pair_star("xxyy")
        'x*xy*y'
        >>> pair_star("aaaa")
        'a*a*a*a'
    """
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + "*" + pair_star(s[1:])
    return s[0] + pair_star(s[1:])


if __name__ == "__main__":
    print(pair_star("hello"))
    print(pair_star("xxyy"))
    print(pair_star("aaaa"))
