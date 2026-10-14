"""Recursion-1: all_star problem solution."""


def all_star(s: str) -> str:
    """Return a new string where all adjacent chars are separated by '*'.

    Args:
        s: Input string.

    Returns:
        String with '*' between every adjacent character.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> all_star("hello")
        'h*e*l*l*o'
        >>> all_star("abc")
        'a*b*c'
        >>> all_star("ab")
        'a*b'
    """

    return s[0] + "*" + all_star(s[1:]) if len(s) > 1 else s


if __name__ == "__main__":
    print(all_star("hello"))
    print(all_star("abc"))
    print(all_star("ab"))
