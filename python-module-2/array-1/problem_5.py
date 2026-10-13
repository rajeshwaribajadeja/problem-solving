"""Array-1: start1 problem solution."""


def start1(a: list, b: list) -> int:
    """Return how many of the given arrays have 1 as their first element.

    Start with 2 int arrays, a and b, of any length. Return how many of
    the arrays have 1 as their first element.

    Args:
        a: First list of integers.
        b: Second list of integers.

    Returns:
        Count of arrays starting with 1 (0, 1, or 2).

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> start1([1, 2, 3], [1, 3])
        2
        >>> start1([7, 2, 3], [1])
        1
        >>> start1([1, 2], [])
        1
    """
    return sum(bool(x) and x[0] == 1 for x in (a, b))


if __name__ == "__main__":
    print(start1([1, 2, 3], [1, 3]))
    print(start1([7, 2, 3], [1]))
    print(start1([1, 2], []))
