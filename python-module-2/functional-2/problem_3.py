"""Functional-2: no_teen problem solution."""


def no_teen(nums: list) -> list:
    """Return a list of integers omitting any between 13 and 19 inclusive.

    Args:
        nums: List of integers.

    Returns:
        List of integers not in the range [13, 19].

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> no_teen([12, 13, 19, 20])
        [12, 20]
        >>> no_teen([1, 14, 1])
        [1, 1]
        >>> no_teen([15])
        []
    """

    return list(filter(lambda x: x < 13 or x > 19, nums))


if __name__ == "__main__":
    print(no_teen([12, 13, 19, 20]))
    print(no_teen([1, 14, 1]))
    print(no_teen([15]))
