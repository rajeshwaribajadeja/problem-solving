"""Recursion-1: array_6 problem solution."""


def array_6(nums: list, index: int) -> bool:
    """Return True if the array contains a 6 at or after the given index.

    Args:
        nums: List of integers.
        index: Starting index in nums.

    Returns:
        True if 6 is found at or after index, False otherwise.

    Complexity:
        Time Complexity: O(n) where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> array_6([1, 6, 4], 0)
        True
        >>> array_6([1, 4], 0)
        False
        >>> array_6([6], 0)
        True
    """
    if index >= len(nums):
        return False
    if nums[index] == 6:
        return True
    return array_6(nums, index + 1)


if __name__ == "__main__":
    print(array_6([1, 6, 4], 0))
    print(array_6([1, 4], 0))
    print(array_6([6], 0))
