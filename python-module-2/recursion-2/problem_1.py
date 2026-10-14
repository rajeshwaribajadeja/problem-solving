"""Recursion-2: group_sum problem solution."""


def group_sum(start: int, nums: list, target: int) -> bool:
    """Return True if a subset of nums starting at index sums to target.

    Given an array of ints, determine if it is possible to choose a
    group of some of the ints such that the group sums to the given
    target using recursive backtracking.

    Args:
        start: Starting index in nums.
        nums: List of integers.
        target: Target sum.

    Returns:
        True if a group sums to target, False otherwise.

    Complexity:
        Time Complexity: O(2^n) in the worst case where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> group_sum(0, [2, 4, 8], 10)
        True
        >>> group_sum(0, [2, 4, 8], 14)
        True
        >>> group_sum(0, [2, 4, 8], 9)
        False
    """
    if start == len(nums):
        return target == 0

    if group_sum(start + 1, nums, target - nums[start]):
        return True

    return group_sum(start + 1, nums, target)


if __name__ == "__main__":
    print(group_sum(0, [2, 4, 8], 10))
    print(group_sum(0, [2, 4, 8], 14))
    print(group_sum(0, [2, 4, 8], 9))
