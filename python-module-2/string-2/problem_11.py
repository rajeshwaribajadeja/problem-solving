"""String-2: one_two problem solution."""


def one_two(s: str) -> str:
    """Move first char after next 2 chars for each 3-char group.

    Given a string, compute a new string by moving the first char to
    come after the next two chars, so "abc" yields "bca". Repeat this
    process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd".
    Ignore any group of fewer than 3 chars at the end.

    Args:
        s: The input string.

    Returns:
        The transformed string where groups of 3 are permuted (123 -> 231).

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the result.

    Examples:
        >>> one_two("abc")
        'bca'
        >>> one_two("tca")
        'cat'
        >>> one_two("tcagdo")
        'catdog'
    """
    return "".join(s[i + 1:i + 3] + s[i] for i in range(0, len(s) - 2, 3))


if __name__ == "__main__":
    print(one_two("abc"))
    print(one_two("tca"))
    print(one_two("tcagdo"))
