"""String-2: star_out problem solution."""


def star_out(s: str) -> str:
    """Remove every star (*) and the characters immediately to its left and right.

    Return a version of the given string, where for every star (*) in
    the string the star and the chars immediately to its left and right
    are gone.

    Args:
        s: The input string.

    Returns:
        The string with '*' and its adjacent characters removed.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the result.

    Examples:
        >>> star_out("ab*cd")
        'ad'
        >>> star_out("ab**cd")
        'ad'
        >>> star_out("sm*eilly")
        'silly'
    """
    result = []
    for i in range(len(s)):
        if s[i] == "*":
            continue
        if i > 0 and s[i - 1] == "*":
            continue
        if i < len(s) - 1 and s[i + 1] == "*":
            continue
        result.append(s[i])
    return "".join(result)


if __name__ == "__main__":
    print(star_out("ab*cd"))
    print(star_out("ab**cd"))
    print(star_out("sm*eilly"))
