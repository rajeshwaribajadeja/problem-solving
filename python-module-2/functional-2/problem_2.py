"""Functional-2: no_9 problem solution."""


def no_9(nums: list) -> list:
    """Return a list of non-negative integers omitting any that end in 9.

    Args:
        nums: List of non-negative integers.

    Returns:
        List of integers from nums that do not end in 9.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> no_9([1, 2, 19])
        [1, 2]
        >>> no_9([9, 19, 29, 3])
        [3]
        >>> no_9([1, 2, 3])
        [1, 2, 3]
    """

    return list(filter(lambda x: x % 10 != 9, nums))


    print(no_9([1, 2, 19]))
    print(no_9([9, 19, 29, 3]))
    print(no_9([1, 2, 3]))
