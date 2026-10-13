"""Array-1: make2 problem solution."""


def make2(a: list, b: list) -> list:
    """Return a new array of length 2 containing elements from a then b.

    Given 2 int arrays, a and b, return a new array length 2 containing,
    as much as will fit, the elements from a followed by the elements from b.

    Args:
        a: First list of integers.
        b: Second list of integers.

    Returns:
        A list of length 2 containing elements from a then b.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> make2([4, 5], [1, 2, 3])
        [4, 5]
        >>> make2([4], [1, 2, 3])
        [4, 1]
        >>> make2([], [1, 2])
        [1, 2]
    """
    return (a + b)[:2]


if __name__ == "__main__":
    print(make2([4, 5], [1, 2, 3]))
    print(make2([4], [1, 2, 3]))
    print(make2([], [1, 2]))
