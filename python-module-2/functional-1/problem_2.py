"""Functional-1: square problem solution."""


def square(nums: list) -> list:
    """Return a list where each integer is multiplied with itself.

    Args:
        nums: List of integers.

    Returns:
        List of integers squared.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> square([1, 2, 3])
        [1, 4, 9]
        >>> square([6, 8, -6, -8, 1])
        [36, 64, 36, 64, 1]
        >>> square([])
        []
    """

    return list(map(lambda x: x * x, nums))


if __name__ == "__main__":
    print(square([1, 2, 3]))
    print(square([6, 8, -6, -8, 1]))
    print(square([]))
