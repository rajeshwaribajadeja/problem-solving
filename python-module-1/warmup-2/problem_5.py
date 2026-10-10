"""Warmup-2: last2 problem solution."""


def last2(s: str) -> int:
    """Count occurrences of the string's last 2 chars throughout the string.

    Given a string, return the count of the number of times that a
    substring of length 2 appears in the string and also as the last 2
    chars of the string (excluding the final substring itself).

    Args:
        s: The input string.

    Returns:
        The count of matching 2-character substrings.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> last2('hixxhi')
        1
        >>> last2('xaxxaxaxx')
        1
        >>> last2('axxxaaxx')
        2
    """
    return s[:-2].count(s[-2:]) if len(s) >= 2 else 0


if __name__ == "__main__":
    print(last2("hixxhi"))
    print(last2("xaxxaxaxx"))
    print(last2("axxxaaxx"))
