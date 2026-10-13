"""Array-3: can_balance problem solution."""


def can_balance(nums: list) -> bool:
    """Return True if array can be split into two parts with equal sum.

    Given a non-empty array, return True if there is a place to split
    the array so that the sum of the numbers on one side is equal to
    the sum of the numbers on the other side.

    Args:
        nums: A non-empty list of integers.

    Returns:
        True if the array can be balanced into two equal sums,
        False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> can_balance([1, 1, 1, 2, 1])
        True
        >>> can_balance([2, 1, 1, 2, 1])
        False
        >>> can_balance([10, 10])
        True
    """
    total = sum(nums)
    left_sum = 0

    for num in nums:
        left_sum += num
        if left_sum * 2 == total:
            return True

    return False


if __name__ == "__main__":
    print(can_balance([1, 1, 1, 2, 1]))
    print(can_balance([2, 1, 1, 2, 1]))
    print(can_balance([10, 10]))
