"""List-2: big_diff problem solution."""


def big_diff(nums: list) -> int:
    """Return the difference between the largest and smallest values.

    Given an array length 1 or more of ints, return the difference
    between the largest and smallest values in the array.

    Args:
        nums: A list of integers (length >= 1).

    Returns:
        The difference between max(nums) and min(nums).

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> big_diff([10, 3, 5, 6])
        7
        >>> big_diff([7, 2, 10, 9])
        8
        >>> big_diff([2, 10, 7, 2])
        8
    """
    return max(nums) - min(nums)


if __name__ == "__main__":
    print(big_diff([10, 3, 5, 6]))
    print(big_diff([7, 2, 10, 9]))
    print(big_diff([2, 10, 7, 2]))