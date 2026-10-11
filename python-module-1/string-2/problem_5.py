"""String-2: end_other problem solution."""


def end_other(a: str, b: str) -> bool:
    """Return True if one string appears at the very end of the other, case-insensitive.

    Given two strings, return True if one of the strings appears at the
    very end of the other string, ignoring upper/lower case differences.

    Args:
        a: First string.
        b: Second string.

    Returns:
        True if either string ends with the other (case-insensitive), False otherwise.

    Complexity:
        Time Complexity: O(len(a) + len(b)) to convert to lower case and check suffix.
        Space Complexity: O(len(a) + len(b)) for lowercased strings.

    Examples:
        >>> end_other('Hiabc', 'abc')
        True
        >>> end_other('Abc', 'Hiabc')
        True
        >>> end_other('abc', 'abXabc')
        True
    """
    return a.lower() in b.lower()[-len(a):] or b.lower() in a.lower()[-len(b):]

if __name__ == "__main__":
    print(end_other("Hiabc", "abc"))
    print(end_other("Abc", "Hiabc"))
    print(end_other("abc", "abXabc"))
