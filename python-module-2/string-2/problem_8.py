"""String-2: xyz_middle problem solution."""


def xyz_middle(s: str) -> bool:
    """Return True if 'xyz' appears in the middle of the string.

    Given a string, does "xyz" appear in the middle of the string?
    To define middle, we'll say that the number of chars to the left
    and right of the "xyz" must differ by at most one.

    Args:
        s: The input string.

    Returns:
        True if "xyz" appears within 1 character of the center, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> xyz_middle("AAxyzBB")
        True
        >>> xyz_middle("AxyzBB")
        True
        >>> xyz_middle("AxyzBBB")
        False
    """
    return any(s[i:i+3] == "xyz" and abs(i - (len(s) - i - 3)) <= 1 for i in range(len(s) - 2))


if __name__ == "__main__":
    print(xyz_middle("AAxyzBB"))
    print(xyz_middle("AxyzBB"))
    print(xyz_middle("AxyzBBB"))