"""Recursion-1: array_220 problem solution."""


def array_220(nums: list, index: int) -> bool:
    """Return True if any value is followed immediately by that value * 10.

    Args:
        nums: List of integers.
        index: Starting index in nums.

    Returns:
        True if such an adjacent pair exists, False otherwise.

    Complexity:
        Time Complexity: O(n) where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> array_220([1, 2, 20], 0)
        True
        >>> array_220([3, 30], 0)
        True
        >>> array_220([3], 0)
        False
    """
    if index >= len(nums) - 1:
        return False
    if nums[index + 1] == nums[index] * 10:
        return True
    return array_220(nums, index + 1)


if __name__ == "__main__":
    print(array_220([1, 2, 20], 0))
    print(array_220([3, 30], 0))
    print(array_220([3], 0))
