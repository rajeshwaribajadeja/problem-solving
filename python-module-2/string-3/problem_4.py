"""String-3: g_happy problem solution."""


def g_happy(s: str) -> bool:
    """Return True if all lowercase 'g' characters have adjacent 'g's.

    We'll say that a lowercase 'g' in a string is "happy" if there is
    another 'g' immediately to its left or right. Return True if all
    the g's in the given string are happy.

    Args:
        s: The input string.

    Returns:
        True if every 'g' has an adjacent 'g', False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> g_happy("xxggxx")
        True
        >>> g_happy("xxgxx")
        False
        >>> g_happy("xxggyygxx")
        False
    """
    for i in range(len(s)):
        if s[i] == "g":
            if (i == 0 or s[i - 1] != "g") and (i == len(s) - 1 or s[i + 1] != "g"):
                return False
    return True


if __name__ == "__main__":
    print(g_happy("xxggxx"))
    print(g_happy("xxgxx"))
    print(g_happy("xxggyygxx"))