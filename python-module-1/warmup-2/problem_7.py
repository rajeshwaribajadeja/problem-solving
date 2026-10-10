"""Warmup-2: array_front9 problem solution."""


def array_front9(nums: list) -> bool:
    """Return True if one of the first 4 elements in the array is a 9.

    Given an array of ints, return True if one of the first 4 elements
    in the array is a 9. The array length may be less than 4.

    Args:
        nums: A list of integers.

    Returns:
        True if 9 appears in the first 4 elements, False otherwise.

    Complexity:
        Time Complexity: O(1) (checks at most the first 4 elements).
        Space Complexity: O(1) (slice is bounded to at most 4 items).

    Examples:
        >>> array_front9([1, 2, 9, 3, 4])
        True
        >>> array_front9([1, 2, 3, 4, 9])
        False
        >>> array_front9([1, 2, 3, 4, 5])
        False
    """
    return 9 in nums[:4]


if __name__ == "__main__":
    print(array_front9([1, 2, 9, 3, 4]))
    print(array_front9([1, 2, 3, 4, 9]))
    print(array_front9([1, 2, 3, 4, 5]))