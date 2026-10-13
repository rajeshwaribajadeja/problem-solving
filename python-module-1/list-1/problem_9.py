"""List-1: sum2 problem solution."""


def sum2(nums: list) -> int:
    """Return the sum of the first 2 elements in the array.

    Given an array of ints, return the sum of the first 2 elements in the
    array. If the array length is less than 2, just sum up the elements
    that exist, returning 0 if the array is length 0.

    Args:
        nums: A list of integers.

    Returns:
        The sum of up to the first 2 elements, or 0 if empty.

    Complexity:
        Time Complexity: O(N)
        Space Complexity: O(1)

    Examples:
        >>> sum2([1, 2, 3])
        3
        >>> sum2([1, 1])
        2
        >>> sum2([1, 1, 1, 1])
        2
    """
    return sum(nums[:2])


if __name__ == "__main__":
    print(sum2([1, 2, 3]))
    print(sum2([1, 1]))
    print(sum2([1, 1, 1, 1]))
