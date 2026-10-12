"""String-3: max_block problem solution."""


def max_block(s: str) -> int:
    """Return the length of the largest block of identical adjacent characters.

    Given a string, return the length of the largest "block" in the string.
    A block is a run of adjacent chars that are the same.

    Args:
        s: The input string.

    Returns:
        Length of the largest block of repeated characters.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> max_block("hoopla")
        2
        >>> max_block("abbCCCddBBBxx")
        3
        >>> max_block("")
        0
    """
    if not s:
        return 0

    max_len = 1
    block_len = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            block_len += 1
        else:
            block_len = 1

        if block_len > max_len:
            max_len = block_len

    return max_len


if __name__ == "__main__":
    print(max_block("hoopla"))
    print(max_block("abbCCCddBBBxx"))
    print(max_block(""))