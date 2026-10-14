"""Functional-2: no_neg problem solution."""


def no_neg(nums: list) -> list:
    """Return a list of integers omitting any that are less than 0.

    Args:
        nums: List of integers.

    Returns:
        List of non-negative integers from nums.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> no_neg([1, -2])
        [1]
        >>> no_neg([-3, -3, 3, 3])
        [3, 3]
        >>> no_neg([-1, -1, -1])
        []
    """

    return list(filter(lambda x: x >= 0, nums))

if __name__ == "__main__":
    print(no_neg([1, -2]))
    print(no_neg([-3, -3, 3, 3]))
    print(no_neg([-1, -1, -1]))

