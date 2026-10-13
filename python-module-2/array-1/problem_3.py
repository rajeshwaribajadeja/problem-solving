"""Array-1: double23 problem solution."""


def double23(nums: list) -> bool:
    """Return True if the array contains 2 twice or 3 twice.

    Given an int array, return True if the array contains 2 twice,
    or 3 twice. The array will be length 0, 1, or 2.

    Args:
        nums: A list of integers (length 0, 1, or 2).

    Returns:
        True if 2 or 3 appears twice, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> double23([2, 2])
        True
        >>> double23([3, 3])
        True
        >>> double23([2, 3])
        False
    """
    return nums.count(2) == 2 or nums.count(3) == 2


if __name__ == "__main__":
    print(double23([2, 2]))
    print(double23([3, 3]))
    print(double23([2, 3]))
