"""Recursion-2: group_sum_6 problem solution."""


def group_sum_6(start: int, nums: list, target: int) -> bool:
    """Return True if a subset sums to target with all 6's chosen.

    Given an array of ints, determine if it is possible to choose a
    group of some of the ints such that the group sums to the given
    target, with the constraint that all 6's must be chosen.

    Args:
        start: Starting index in nums.
        nums: List of integers.
        target: Target sum.

    Returns:
        True if a valid subset sums to target, False otherwise.

    Complexity:
        Time Complexity: O(2^n) in the worst case where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> group_sum_6(0, [5, 6, 2], 8)
        True
        >>> group_sum_6(0, [5, 6, 2], 9)
        False
        >>> group_sum_6(0, [5, 6, 2], 7)
        False
    """
    if start == len(nums):
        return target == 0

    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - 6)

    if group_sum_6(start + 1, nums, target - nums[start]):
        return True

    return group_sum_6(start + 1, nums, target)


if __name__ == "__main__":
    print(group_sum_6(0, [5, 6, 2], 8))
    print(group_sum_6(0, [5, 6, 2], 9))
    print(group_sum_6(0, [5, 6, 2], 7))
