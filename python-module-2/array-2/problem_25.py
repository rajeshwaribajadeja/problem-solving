"""Array-2: without_ten problem solution."""


def without_ten(nums: list) -> list:
    """Return array with all 10s removed, shifting left and trailing zeros.

    Return a version of the given array where all the 10's have been
    removed. The remaining elements should shift left towards the start
    of the array as needed, and the empty spaces at the end should be 0.

    Args:
        nums: A list of integers.

    Returns:
        The array without 10s and padded with trailing zeros to
        original length.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> without_ten([1, 10, 10, 2])
        [1, 2, 0, 0]
        >>> without_ten([10, 2, 10])
        [2, 0, 0]
        >>> without_ten([1, 99, 10])
        [1, 99, 0]
    """
    return [x for x in nums if x != 10] + [0] * nums.count(10)


if __name__ == "__main__":
    print(without_ten([1, 10, 10, 2]))
    print(without_ten([10, 2, 10]))
    print(without_ten([1, 99, 10]))
