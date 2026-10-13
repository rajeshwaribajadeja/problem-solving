"""Array-2: lucky13 problem solution."""


def lucky13(nums: list) -> bool:
    """Return True if the array contains no 1s and no 3s.

    Given an array of ints, return True if the array contains no 1's
    and no 3's.

    Args:
        nums: A list of integers.

    Returns:
        True if neither 1 nor 3 is present, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> lucky13([0, 2, 4])
        True
        >>> lucky13([1, 2, 3])
        False
        >>> lucky13([1, 2, 4])
        False
    """
    return 1 not in nums and 3 not in nums


if __name__ == "__main__":
    print(lucky13([0, 2, 4]))
    print(lucky13([1, 2, 3]))
    print(lucky13([1, 2, 4]))
