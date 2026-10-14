"""Recursion-2: split_53 problem solution."""


def split_53(nums: list) -> bool:
    """Return True if nums can split with 5s in one group and 3s in other.

    Given an array of ints, determine if it is possible to divide the
    ints into two groups such that the sum of the two groups is the
    same, with these constraints: all multiples of 5 must be in one
    group, and all multiples of 3 (not 5) must be in the other.

    Args:
        nums: List of integers.

    Returns:
        True if such an equal split is possible, False otherwise.

    Complexity:
        Time Complexity: O(2^n) in the worst case where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> split_53([1, 1])
        True
        >>> split_53([1, 1, 1])
        False
        >>> split_53([2, 4, 2])
        True
    """
    def helper(index: int, group_1: int, group_2: int) -> bool:
        if index == len(nums):
            return group_1 == group_2

        if nums[index] % 5 == 0:
            return helper(index + 1, group_1 + nums[index], group_2)

        if nums[index] % 3 == 0:
            return helper(index + 1, group_1, group_2 + nums[index])

        if helper(index + 1, group_1 + nums[index], group_2):
            return True

        return helper(index + 1, group_1, group_2 + nums[index])

    return helper(0, 0, 0)


if __name__ == "__main__":
    print(split_53([1, 1]))
    print(split_53([1, 1, 1]))
    print(split_53([2, 4, 2]))
