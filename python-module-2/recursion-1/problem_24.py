"""Recursion-1: string_clean problem solution."""


def string_clean(s: str) -> str:
    """Return string where identical adjacent chars are reduced to one.

    Args:
        s: Input string.

    Returns:
        Cleaned string without duplicate adjacent characters.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> string_clean("yyzzza")
        'yza'
        >>> string_clean("abbbcdd")
        'abcd'
        >>> string_clean("Hello")
        'Helo'
    """
    return s if len(s) <=1 else string_clean(s[1:]) if s[0] == s[1] else s[0] + string_clean(s[1:])


if __name__ == "__main__":
    print(string_clean("yyzzza"))
    print(string_clean("abbbcdd"))
    print(string_clean("Hello"))
