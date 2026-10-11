"""String-1: middletwo problem solution."""


def middletwo(s: str) -> str:
    """Return a string made of the middle two characters of an even-length string.

    Given a string of even length, return a string made of the middle
    two chars, so the string "string" yields "ri". The string length
    will be at least 2.

    Args:
        s: An even-length string of length 2 or more.

    Returns:
        A string of the middle 2 characters.

    Complexity:
        Time Complexity: O(1) (extracts exactly 2 characters).
        Space Complexity: O(1)

    Examples:
        >>> middletwo("string")
        'ri'
        >>> middletwo("code")
        'od'
        >>> middletwo("Practice")
        'ct'
    """
    mid = len(s) // 2
    return s[mid - 1:mid + 1]


if __name__ == "__main__":
    print(middletwo("string"))
    print(middletwo("code"))
    print(middletwo("Practice"))