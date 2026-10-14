"""Recursion-1: power_n problem solution."""


def power_n(base: int, n: int) -> int:
    """Return base raised to the power n computed recursively.

    Args:
        base: The base integer (base >= 1).
        n: The exponent (n >= 1).

    Returns:
        base raised to power n.

    Complexity:
        Time Complexity: O(n) recursive calls.
        Space Complexity: O(n) auxiliary space for the call stack.

    Examples:
        >>> power_n(3, 1)
        3
        >>> power_n(3, 2)
        9
        >>> power_n(3, 3)
        27
    """
    return base if n <= 1 else base * power_n(base, n - 1)


if __name__ == "__main__":
    print(power_n(3, 1))
    print(power_n(3, 2))
    print(power_n(3, 3))
