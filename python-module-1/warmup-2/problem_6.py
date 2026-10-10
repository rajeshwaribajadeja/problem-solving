"""Warmup-2: array_count9 problem solution."""


def array_count9(nums: list[int]) -> int:
    """Return the number of 9's in the array.

    Given an array of ints, return the count of the number 9 appearing
    in the array.

    Args:
        nums: A list of integers.

    Returns:
        The count of 9's in the list.

    Complexity:
        Time Complexity: O(N) where N is the length of nums.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> array_count9([1, 2, 9])
        1
        >>> array_count9([1, 9, 9])
        2
        >>> array_count9([1, 9, 9, 3, 9])
        3
    """
    return nums.count(9)


if __name__ == "__main__":
    print(array_count9([1, 2, 9]))
    print(array_count9([1, 9, 9]))
    print(array_count9([1, 9, 9, 3, 9]))