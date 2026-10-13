"""Array-2: sum28 problem solution."""


def sum28(nums: list) -> bool:
    """Return True if the sum of all 2s in the array is exactly 8.

    Given an array of ints, return True if the sum of all the 2's
    in the array is exactly 8.

    Args:
        nums: A list of integers.

    Returns:
        True if the sum of all 2s is exactly 8, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> sum28([2, 3, 2, 2, 4, 2])
        True
        >>> sum28([2, 3, 2, 2, 4, 2, 2])
        False
        >>> sum28([1, 2, 3, 4])
        False
    """
    return nums.count(2) * 2 == 8


if __name__ == "__main__":
    print(sum28([2, 3, 2, 2, 4, 2]))
    print(sum28([2, 3, 2, 2, 4, 2, 2]))
    print(sum28([1, 2, 3, 4]))
