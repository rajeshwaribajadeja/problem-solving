"""Logic-2: evenly_spaced problem solution."""


def evenly_spaced(a: int, b: int, c: int) -> bool:
    """Determine whether three integers are evenly spaced.

    Given three ints, a b c, one of them is small, one is medium and
    one is large. Return True if the three values are evenly spaced, so
    the difference between small and medium is the same as the difference
    between medium and large.

    Args:
        a: First integer.
        b: Second integer.
        c: Third integer.

    Returns:
        True if the three values are evenly spaced, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> evenly_spaced(2, 4, 6)
        True
        >>> evenly_spaced(4, 6, 2)
        True
        >>> evenly_spaced(4, 6, 3)
        False
    """
    small, medium, large = sorted((a, b, c))
    return medium - small == large - medium


if __name__ == "__main__":
    print(evenly_spaced(2, 4, 6))
    print(evenly_spaced(4, 6, 2))
    print(evenly_spaced(4, 6, 3))