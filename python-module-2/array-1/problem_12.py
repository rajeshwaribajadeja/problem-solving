"""Array-1: front_piece problem solution."""


def front_piece(nums: list) -> list:
    """Return a new array of the first 2 elements or all if length < 2.

    Given an int array of any length, return a new array of its first
    2 elements. If the array is smaller than length 2, use whatever
    elements are present.

    Args:
        nums: A list of integers.

    Returns:
        A list of up to the first 2 elements of the array.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> front_piece([1, 2, 3])
        [1, 2]
        >>> front_piece([1, 2])
        [1, 2]
        >>> front_piece([1])
        [1]
    """
    return nums[:2]


if __name__ == "__main__":
    print(front_piece([1, 2, 3]))
    print(front_piece([1, 2]))
    print(front_piece([1]))
