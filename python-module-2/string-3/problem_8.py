"""String-3: mirror_ends problem solution."""


def mirror_ends(s: str) -> str:
    """Return the longest prefix that mirrors the suffix backwards.

    Given a string, look for a mirror image (backwards) string at both
    the beginning and end of the given string.

    Args:
        s: The input string.

    Returns:
        The mirror-matched prefix substring.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the result.

    Examples:
        >>> mirror_ends("abXYZba")
        'ab'
        >>> mirror_ends("abca")
        'a'
        >>> mirror_ends("aba")
        'aba'
    """
    result = []
    for i in range(len(s)):
        if s[i] == s[-(i + 1)]:
            result.append(s[i])
        else:
            break
    return "".join(result)


if __name__ == "__main__":
    print(mirror_ends("abXYZba"))
    print(mirror_ends("abca"))
    print(mirror_ends("aba"))
