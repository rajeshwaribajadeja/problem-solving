"""String-2: count_code problem solution."""


def count_code(s: str) -> int:
    """Return the number of times that 'co?e' appears in the given string.

    Return the number of times that the pattern "co?e" appears in the
    given string, where '?' can be any character.

    Args:
        s: The input string.

    Returns:
        The count of matching 'co?e' substrings.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> count_code('aaacodebbb')
        1
        >>> count_code('codexxcode')
        2
        >>> count_code('cozexxcope')
        2
    """
    return sum(
        1 for i in range(len(s) - 3) if s[i:i + 2] == "co" and s[i + 3] == "e"
    )


if __name__ == "__main__":
    print(count_code("aaacodebbb"))
    print(count_code("codexxcode"))
    print(count_code("cozexxcope"))
