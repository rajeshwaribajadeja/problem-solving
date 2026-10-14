"""Warmup-2: string_yak problem solution."""


def string_yak(s: str) -> str:
    """Return string with all 'y.k' patterns removed.

    Args:
        s: Input string.

    Returns:
        String with all occurrences of 'y<any_char>k' removed.

    Complexity:
        Time Complexity: O(n) where n is the length of s.
        Space Complexity: O(n) for the newly constructed string.

    Examples:
        >>> string_yak("yakpak")
        'pak'
        >>> string_yak("pakyak")
        'pak'
        >>> string_yak("yak123ya")
        '123ya'
    """
    result = []
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i] == "y" and s[i + 2] == "k":
            i += 3
        else:
            result.append(s[i])
            i += 1
    return "".join(result)


if __name__ == "__main__":
    print(string_yak("yakpak"))
    print(string_yak("pakyak"))
    print(string_yak("yak123ya"))