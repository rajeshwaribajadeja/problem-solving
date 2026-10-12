"""String-2: prefix_again problem solution."""


def prefix_again(s: str, n: int) -> bool:
    """Return True if prefix of first n chars appears elsewhere in the string.

    Given a string, consider the prefix string made of the first N
    chars of the string. Return True if that prefix string appears
    somewhere else in the string. Assume 1 <= n <= len(s).

    Args:
        s: The non-empty input string.
        n: The length of the prefix to match.

    Returns:
        True if the prefix appears again later in s, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> prefix_again("abXYabc", 1)
        True
        >>> prefix_again("abXYabc", 2)
        True
        >>> prefix_again("abXYabc", 3)
        False
    """
    return s[:n] in s[n:]


if __name__ == "__main__":
    print(prefix_again("abXYabc", 1))
    print(prefix_again("abXYabc", 2))
    print(prefix_again("abXYabc", 3))