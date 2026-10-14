"""Functional-1: math_1 problem solution."""


def math_1(nums: list) -> list:
    """Return a list where each integer is added to 1 and multiplied by 10.

    Args:
        nums: List of integers.

    Returns:
        List of integers transformed by (x + 1) * 10.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> math_1([1, 2, 3])
        [20, 30, 40]
        >>> math_1([6, 8, 6, 8, 1])
        [70, 90, 70, 90, 20]
        >>> math_1([10])
        [110]
    """

    return list(map(lambda x: (x + 1) * 10, nums))


if __name__ == "__main__":
    print(math_1([1, 2, 3]))
    print(math_1([6, 8, 6, 8, 1]))
    print(math_1([10]))
