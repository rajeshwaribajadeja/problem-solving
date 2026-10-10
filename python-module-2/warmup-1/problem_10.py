"""Warmup-1: del_del problem solution."""


def del_del(s: str) -> str:
    """Delete 'del' if it appears starting at index 1 of the string.

    Given a string, if the string "del" appears starting at index 1,
    return a string where that "del" has been deleted. Otherwise,
    return the string unchanged.

    Args:
        s: The input string.

    Returns:
        The string with "del" at index 1 removed, or the original string.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting string.

    Examples:
        >>> del_del("adelbc")
        'abc'
        >>> del_del("adelHello")
        'aHello'
        >>> del_del("adedbc")
        'adedbc'
    """
    return s[:1] + s[4:] if s[1:4] == "del" else s


if __name__ == "__main__":
    print(del_del("adelbc"))
    print(del_del("adelHello"))
    print(del_del("adedbc"))