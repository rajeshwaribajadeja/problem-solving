"""Functional-1: doubling problem solution."""


def doubling(nums: list) -> list:
    """Return a list where each integer is multiplied by 2.

    Args:
        nums: List of integers.

    Returns:
        List of integers with each element doubled.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> doubling([1, 2, 3])
        [2, 4, 6]
        >>> doubling([6, 8, 6, 8, -1])
        [12, 16, 12, 16, -2]
        >>> doubling([])
        []
    """

    return list(map(lambda x: x * 2, nums))


if __name__ == "__main__":
    print(doubling([1, 2, 3]))
    print(doubling([6, 8, 6, 8, -1]))
    print(doubling([]))
