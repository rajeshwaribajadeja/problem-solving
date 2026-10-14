"""Recursion-2: split_odd_10 problem solution."""


def split_odd_10(nums: list) -> bool:
    """Return True if nums can split into one group % 10 == 0 and other odd.

    Given an array of ints, determine if it is possible to divide the
    ints into two groups, so that the sum of one group is a multiple
    of 10, and the sum of the other group is odd.

    Args:
        nums: List of integers.

    Returns:
        True if such a split is possible, False otherwise.

    Complexity:
        Time Complexity: O(2^n) in the worst case where n is len(nums).
        Space Complexity: O(n) auxiliary space for recursion call stack.

    Examples:
        >>> split_odd_10([5, 5, 5])
        True
        >>> split_odd_10([5, 5, 6])
        False
        >>> split_odd_10([5, 5, 6, 1])
        True
    """
    def helper(index: int, sum_10: int, sum_odd: int) -> bool:
        if index == len(nums):
            return sum_10 % 10 == 0 and sum_odd % 2 == 1

        if helper(index + 1, sum_10 + nums[index], sum_odd):
            return True

        return helper(index + 1, sum_10, sum_odd + nums[index])

    return helper(0, 0, 0)


if __name__ == "__main__":
    print(split_odd_10([5, 5, 5]))
    print(split_odd_10([5, 5, 6]))
    print(split_odd_10([5, 5, 6, 1]))
