"""Array-1: plus_two problem solution."""


def plus_two(a: list, b: list) -> list:
    """Concatenate two length-2 arrays into a new array of length 4.

    Given 2 int arrays, each length 2, return a new array length 4
    containing all their elements.

    Args:
        a: First list of 2 integers.
        b: Second list of 2 integers.

    Returns:
        A list of length 4 containing elements of a followed by b.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> plus_two([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> plus_two([4, 4], [2, 2])
        [4, 4, 2, 2]
        >>> plus_two([9, 2], [3, 4])
        [9, 2, 3, 4]
    """
    return a + b


if __name__ == "__main__":
    print(plus_two([1, 2], [3, 4]))
    print(plus_two([4, 4], [2, 2]))
    print(plus_two([9, 2], [3, 4]))
