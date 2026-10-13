"""Array-1: bigger_two problem solution."""


def bigger_two(a: list, b: list) -> list:
    """Return the array of length 2 which has the largest sum, or a on tie.

    Start with 2 int arrays, a and b, each length 2. Consider the sum of the
    values in each array. Return the array which has the largest sum.
    In event of a tie, return a.

    Args:
        a: First list of 2 integers.
        b: Second list of 2 integers.

    Returns:
        The array with the larger sum, or a in case of a tie.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> bigger_two([1, 2], [3, 4])
        [3, 4]
        >>> bigger_two([3, 4], [1, 2])
        [3, 4]
        >>> bigger_two([1, 1], [1, 2])
        [1, 2]
    """
    return a if sum(a) >= sum(b) else b


if __name__ == "__main__":
    print(bigger_two([1, 2], [3, 4]))
    print(bigger_two([3, 4], [1, 2]))
    print(bigger_two([1, 1], [1, 2]))
