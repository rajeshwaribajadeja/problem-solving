"""Warmup-1: icy_hot problem solution."""


def icy_hot(temp1: int, temp2: int) -> bool:
    """Determine if one temperature is < 0 and the other is > 100.

    Given two temperatures, return True if one is less than 0 and the
    other is greater than 100.

    Args:
        temp1: First temperature value.
        temp2: Second temperature value.

    Returns:
        True if one temp is < 0 and the other > 100, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> icy_hot(120, -1)
        True
        >>> icy_hot(-1, 120)
        True
        >>> icy_hot(2, 120)
        False
    """
    return (temp1 < 0 and temp2 > 100) or (temp1 > 100 and temp2 < 0)


if __name__ == "__main__":
    print(icy_hot(120, -1))
    print(icy_hot(-1, 120))
    print(icy_hot(2, 120))