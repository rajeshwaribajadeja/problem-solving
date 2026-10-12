"""String-3: same_ends problem solution."""


def same_ends(s: str) -> str:
    """Return the longest non-overlapping substring at both beginning and end.

    Given a string, return the longest substring that appears at both
    the beginning and end of the string without overlapping.

    Args:
        s: The input string.

    Returns:
        The longest shared boundary substring.

    Complexity:
        Time Complexity: O(N^2) where N is the length of the string.
        Space Complexity: O(N) to store the result substring.

    Examples:
        >>> same_ends("abXYab")
        'ab'
        >>> same_ends("xx")
        'x'
        >>> same_ends("xxx")
        'x'
    """
    return max((s[:i] for i in range(1, len(s)//2 + 1) if s[:i] == s[-i:]), key=len, default="")


if __name__ == "__main__":
    print(same_ends("abXYab"))
    print(same_ends("xx"))
    print(same_ends("xxx"))
