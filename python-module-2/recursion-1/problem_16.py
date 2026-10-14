"""Recursion-1: array_11 problem solution."""


def array_11(nums: list, index: int) -> int:
    """Return count of 11s in the array at or after the given index.

    Args:
        nums: List of integers.
        index: Starting index in nums.

    Returns:
        Number of times 11 appears at or after index.

    Complexity:
        Time Complexity: O(n) where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> array_11([1, 2, 11], 0)
        1
        >>> array_11([11, 11], 0)
        2
        >>> array_11([1, 2, 3, 4], 0)
        0
    """
    if index >= len(nums):
        return 0
    match = 1 if nums[index] == 11 else 0
    return match + array_11(nums, index + 1)


if __name__ == "__main__":
    print(array_11([1, 2, 11], 0))
    print(array_11([11, 11], 0))
    print(array_11([1, 2, 3, 4], 0))
