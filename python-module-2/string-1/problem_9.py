"""String-1: has_bad problem solution."""


def has_bad(s: str) -> bool:
    """Return True if 'bad' appears starting at index 0 or 1.

    Given a string, return True if "bad" appears starting at index 0 or
    1 in the string, such as with "badxxx" or "xbadxx" but not "xxbadxx".
    The string may be any length, including 0.

    Args:
        s: The input string.

    Returns:
        True if "bad" starts at index 0 or 1, False otherwise.

    Complexity:
        Time Complexity: O(1) (checks at most indices 0 to 3).
        Space Complexity: O(1)

    Examples:
        >>> has_bad("badxx")
        True
        >>> has_bad("xbadxx")
        True
        >>> has_bad("xxbadxx")
        False
    """
    return s[:3] == "bad" or s[1:4] == "bad"


if __name__ == "__main__":
    print(has_bad("badxx"))
    print(has_bad("xbadxx"))
    print(has_bad("xxbadxx"))