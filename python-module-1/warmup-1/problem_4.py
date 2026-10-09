"""Warmup-1: diff21 problem solution."""


def diff21(n: int) -> int:
    """Compute the absolute difference between n and 21, doubled if n is over 21.

    Given an int n, return the absolute difference between n and 21,
    except return double the absolute difference if n is over 21.

    Args:
        n: An integer value.

    Returns:
        The difference between n and 21, or double the difference if n > 21.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> diff21(19)
        2
        >>> diff21(10)
        11
        >>> diff21(21)
        0
    """
    return 2 * abs(21 - n) if n > 21 else abs(n - 21)


if __name__ == "__main__":
    print(diff21(19))
    print(diff21(10))
    print(diff21(21))