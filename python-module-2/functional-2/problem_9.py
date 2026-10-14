"""Functional-2: square_56 problem solution."""


def square_56(nums: list) -> list:
    """Return numbers squared plus 10, omitting any ending in 5 or 6.

    Args:
        nums: List of integers.

    Returns:
        List of resulting integers (x * x + 10) not ending in 5 or 6.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> square_56([3, 1, 4])
        [19, 11]
        >>> square_56([1])
        [11]
        >>> square_56([2])
        [14]
    """

    nums = list(map(lambda x: x * x + 10, nums))

    return list(filter(lambda x: x % 10 != 5 and x % 10 != 6, nums))

if __name__ == "__main__":
    print(square_56([3, 1, 4]))
    print(square_56([1]))
    print(square_56([2]))

