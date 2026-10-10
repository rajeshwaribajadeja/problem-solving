"""Warmup-1: mix_start problem solution."""


def mix_start(s: str) -> bool:
    """Return True if the string begins with 'mix', except 'm' can be anything.

    Return True if the given string begins with "mix", except the 'm'
    can be any character, so "pix", "9ix", etc. all count.

    Args:
        s: The input string.

    Returns:
        True if string has length >= 3 and starts with '?ix', False otherwise.

    Complexity:
        Time Complexity: O(1) (checks at most 3 characters).
        Space Complexity: O(1)

    Examples:
        >>> mix_start("mix snacks")
        True
        >>> mix_start("pix snacks")
        True
        >>> mix_start("piz snacks")
        False
    """
    return len(s) >= 3 and s[1:3] == "ix"


if __name__ == "__main__":
    print(mix_start("mix snacks"))
    print(mix_start("pix snacks"))
    print(mix_start("piz snacks"))