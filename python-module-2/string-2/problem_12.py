"""String-2: zip_zap problem solution."""


def zip_zap(s: str) -> str:
    """Remove middle letter for any length-3 word starting with 'z' and ending with 'p'.

    Look for patterns like "zip" and "zap" in the string -- length-3,
    starting with 'z' and ending with 'p'. Return a string where for all
    such words, the middle letter is gone, so "zipXzap" yields "zpXzp".

    Args:
        s: The input string.

    Returns:
        The string with middle letters removed from 'z?p' patterns.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the transformed string.

    Examples:
        >>> zip_zap("zipXzap")
        'zpXzp'
        >>> zip_zap("zopzop")
        'zpzp'
        >>> zip_zap("zzzopzop")
        'zzzpzp'
    """
    result = []
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i] == "z" and s[i + 2] == "p":
            result.append("zp")
            i += 3
        else:
            result.append(s[i])
            i += 1
    return "".join(result)


if __name__ == "__main__":
    print(zip_zap("zipXzap"))
    print(zip_zap("zopzop"))
    print(zip_zap("zzzopzop"))
