"""Recursion-2: group_no_adj problem solution."""


def group_no_adj(start: int, nums: list, target: int) -> bool:
    """Return True if a subset with no adjacent numbers chosen sums to
    target.

    Given an array of ints, determine if it is possible to choose a
    group of some of the ints such that the group sums to the given
    target, with the constraint that adjacent values must not both be
    chosen.

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
        >>> group_no_adj(0, [2, 5, 10, 4], 12)
        True
        >>> group_no_adj(0, [2, 5, 10, 4], 14)
        False
        >>> group_no_adj(0, [2, 5, 10, 4], 7)
        False
    """
    if target == 0:
        return True

    if start >= len(nums):
        return False

    if group_no_adj(start + 2, nums, target - nums[start]):
        return True

    return group_no_adj(start + 1, nums, target)


if __name__ == "__main__":
    print(group_no_adj(0, [2, 5, 10, 4], 12))
    print(group_no_adj(0, [2, 5, 10, 4], 14))
    print(group_no_adj(0, [2, 5, 10, 4], 7))
