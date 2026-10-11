"""String-1: last_chars problem solution."""


def last_chars(a: str, b: str) -> str:
    """Return string made of first char of a and last char of b, or '@' if empty.

    Given 2 strings, a and b, return a new string made of the first char
    of a and the last char of b, so "yo" and "java" yields "ya". If either
    string is length 0, use '@' for its missing char.

    Args:
        a: First input string.
        b: Second input string.

    Returns:
        A 2-character string combining a's first char and b's last char.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> last_chars("last", "chars")
        'ls'
        >>> last_chars("yo", "java")
        'ya'
        >>> last_chars("hi", "")
        'h@'
    """
    return (a[0] if a else "@") + (b[-1] if b else "@")


if __name__ == "__main__":
    print(last_chars("last", "chars"))
    print(last_chars("yo", "java"))
    print(last_chars("hi", ""))