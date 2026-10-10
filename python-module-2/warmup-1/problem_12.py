"""Warmup-1: start_oz problem solution."""


def start_oz(s: str) -> str:
    """Return a string made of the first 2 chars matching 'o' and 'z'.

    Given a string, return a string made of the first 2 chars (if present);
    however, include the first char only if it is 'o' and include the second
    only if it is 'z'.

    Args:
        s: The input string.

    Returns:
        The resulting filtered prefix string.

    Complexity:
        Time Complexity: O(1) (examines at most 2 characters).
        Space Complexity: O(1) (result string is at most 2 characters).

    Examples:
        >>> start_oz("ozymandias")
        'oz'
        >>> start_oz("bzoo")
        'z'
        >>> start_oz("oxx")
        'o'
    """
    return s[:1] * (s[:1] == "o") + s[1:2] * (s[1:2] == "z")


if __name__ == "__main__":
    print(start_oz("ozymandias"))
    print(start_oz("bzoo"))
    print(start_oz("oxx"))