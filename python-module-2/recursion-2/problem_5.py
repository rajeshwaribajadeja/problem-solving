"""Recursion-2: group_sum_clump problem solution."""


def group_sum_clump(start: int, nums: list, target: int) -> bool:
    """Return True if a subset sums to target with adjacent equals clumped.

    If there are numbers in the array that are adjacent and identical,
    they must either all be chosen, or none of them chosen.

    Args:
        start: Starting index in nums.
        nums: List of integers.
        target: Target sum.

    Returns:
        True if a valid clumped subset sums to target, False otherwise.

    Complexity:
        Time Complexity: O(2^n) in the worst case where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> group_sum_clump(0, [2, 4, 8], 10)
        True
        >>> group_sum_clump(0, [1, 2, 4, 8, 1], 14)
        True
        >>> group_sum_clump(0, [2, 4, 4, 8], 14)
        False
    """
    if target == 0:
        return True

    if start >= len(nums):
        return False

    end = start
    while end < len(nums) and nums[end] == nums[start]:
        end += 1

    clump_sum = nums[start] * (end - start)

    if group_sum_clump(end, nums, target - clump_sum):
        return True

    return group_sum_clump(end, nums, target)


if __name__ == "__main__":
    print(group_sum_clump(0, [2, 4, 8], 10))
    print(group_sum_clump(0, [1, 2, 4, 8, 1], 14))
    print(group_sum_clump(0, [2, 4, 4, 8], 14))
