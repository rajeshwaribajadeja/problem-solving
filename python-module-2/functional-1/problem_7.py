"""Functional-1: right_digit problem solution."""


def right_digit(nums: list) -> list:
    """Return a list of the rightmost digits for each non-negative integer.

    Args:
        nums: List of non-negative integers.

    Returns:
        List containing the rightmost digit (modulo 10) of each integer.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> right_digit([1, 22, 93])
        [1, 2, 3]
        >>> right_digit([16, 8, 886, 8, 1])
        [6, 8, 6, 8, 1]
        >>> right_digit([10, 0])
        [0, 0]
    """

    return list(map(lambda x: x % 10, nums))


if __name__ == "__main__":
    print(right_digit([1, 22, 93]))
    print(right_digit([16, 8, 886, 8, 1]))
    print(right_digit([10, 0]))
