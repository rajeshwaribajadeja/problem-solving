"""Warmup-2: doublex problem solution."""


def doublex(s: str) -> bool:
    """Return True if first instance of 'x' is immediately followed by 'x'.

    Args:
        s: Input string.

    Returns:
        True if first 'x' is followed by another 'x', False otherwise.

    Complexity:
        Time Complexity: O(n) where n is the length of s.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> doublex("axxbb")
        True
        >>> doublex("axaxax")
        False
        >>> doublex("xxxxx")
        True
    """
    i = s.find("x")
    return i != -1 and i + 1 < len(s) and s[i + 1] == "x"


if __name__ == "__main__":
    print(doublex("axxbb"))
    print(doublex("axaxax"))
    print(doublex("xxxxx"))
