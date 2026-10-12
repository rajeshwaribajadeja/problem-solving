"""String-2: same_star_char problem solution."""


def same_star_char(s: str) -> bool:
    """Return True if chars immediately before and after every '*' match.

    Returns True if for every '*' (star) in the string, if there are
    chars both immediately before and after the star, they are the same.

    Args:
        s: The input string.

    Returns:
        True if all surrounding characters around '*' match, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> same_star_char("xy*yzz")
        True
        >>> same_star_char("xy*zzz")
        False
        >>> same_star_char("*xa*az")
        True
    """
    return all(s[i - 1] == s[i + 1] for i in range(1, len(s) - 1) if s[i] == "*")


if __name__ == "__main__":
    print(same_star_char("xy*yzz"))
    print(same_star_char("xy*zzz"))
    print(same_star_char("*xa*az"))
