"""Logic-2: close_far problem solution."""


def close_far(a: int, b: int, c: int) -> bool:
    """Return True if one of b or c is close to a and other is far from both.

    Given three ints, a, b, c, return True if one of b or c is "close"
    (differing from a by at most 1), while the other is "far", differing
    from both other values by 2 or more.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        True if close/far conditions are satisfied, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> close_far(1, 2, 10)
        True
        >>> close_far(1, 2, 3)
        False
        >>> close_far(4, 1, 3)
        True
    """
    b_close = abs(a - b) <= 1
    c_close = abs(a - c) <= 1
    b_far = abs(a - b) >= 2 and abs(c - b) >= 2
    c_far = abs(a - c) >= 2 and abs(b - c) >= 2

    return (b_close and c_far) or (c_close and b_far)


if __name__ == "__main__":
    print(close_far(1, 2, 10))
    print(close_far(1, 2, 3))
    print(close_far(4, 1, 3))
