"""String-2: xyz_there problem solution."""


def xyz_there(s: str) -> bool:
    """Return True if 'xyz' appears without directly being preceded by a period.

    Return True if the given string contains an appearance of "xyz"
    where the "xyz" is not directly preceded by a period (.).

    Args:
        s: The input string.

    Returns:
        True if valid "xyz" without preceding '.' is found, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> xyz_there('abcxyz')
        True
        >>> xyz_there('abc.xyz')
        False
        >>> xyz_there('xyz.abc')
        True 
    """
    return any(
        s[i:i + 3] == "xyz" and (i == 0 or s[i - 1] != ".")
        for i in range(len(s) - 2)
    )


if __name__ == "__main__":
    print(xyz_there("abcxyzabc"))
    print(xyz_there("abc.xyzabc"))
    print(xyz_there("xyzabc.xyz"))
