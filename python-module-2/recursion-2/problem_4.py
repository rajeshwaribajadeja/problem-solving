"""Recursion-2: group_sum_5 problem solution."""


def group_sum_5(start: int, nums: list, target: int) -> bool:
    """Return True if a subset sums to target under multiples of 5 rules.

    All multiples of 5 must be included in the group. If the value
    immediately following a multiple of 5 is 1, it must not be chosen.

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
        >>> group_sum_5(0, [2, 5, 10, 4], 19)
        True
        >>> group_sum_5(0, [2, 5, 10, 4], 17)
        True
        >>> group_sum_5(0, [2, 5, 10, 4], 12)
        False
    """
    if start == len(nums):
        return target == 0

    if nums[start] % 5 == 0:
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])
        return group_sum_5(start + 1, nums, target - nums[start])

    if group_sum_5(start + 1, nums, target - nums[start]):
        return True

    return group_sum_5(start + 1, nums, target)


if __name__ == "__main__":
    print(group_sum_5(0, [2, 5, 10, 4], 19))
    print(group_sum_5(0, [2, 5, 10, 4], 17))
    print(group_sum_5(0, [2, 5, 10, 4], 12))
