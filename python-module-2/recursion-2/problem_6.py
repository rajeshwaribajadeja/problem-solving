"""Recursion-2: split_array problem solution."""


def split_array(nums: list) -> bool:
    """Return True if nums can be split into two groups with equal sums.

    Given an array of ints, determine if it is possible to divide the
    ints into two groups such that the sums of the two groups are equal.
    Every int must be in one group or the other.

    Args:
        nums: List of integers.

    Returns:
        True if an equal-sum split is possible, False otherwise.

    Complexity:
        Time Complexity: O(2^n) in the worst case where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> split_array([2, 2])
        True
        >>> split_array([2, 3])
        False
        >>> split_array([5, 2, 3])
        True
    """
    def helper(index: int, group_1: int, group_2: int) -> bool:
        if index == len(nums):
            return group_1 == group_2

        if helper(index + 1, group_1 + nums[index], group_2):
            return True

        return helper(index + 1, group_1, group_2 + nums[index])

    return helper(0, 0, 0)


if __name__ == "__main__":
    print(split_array([2, 2]))
    print(split_array([2, 3]))
    print(split_array([5, 2, 3]))
