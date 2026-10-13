"""Array-1: front11 problem solution."""


def front11(a: list, b: list) -> list:
    """Return an array with the first element of each non-empty array.

    Given 2 int arrays, a and b, of any length, return a new array with
    the first element of each array. If either array is length 0, ignore
    that array.

    Args:
        a: First list of integers.
        b: Second list of integers.

    Returns:
        A list of length 0, 1, or 2 with the first elements.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> front11([1, 2, 3], [7, 9, 8])
        [1, 7]
        >>> front11([1], [2])
        [1, 2]
        >>> front11([1, 7], [])
        [1]
    """
    return a[:1] + b[:1]


if __name__ == "__main__":
    print(front11([1, 2, 3], [7, 9, 8]))
    print(front11([1], [2]))
    print(front11([1, 7], []))
