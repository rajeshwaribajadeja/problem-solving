"""Array-2: shift_left problem solution."""


def shift_left(nums: list) -> list:
    """Return an array that is left shifted by one element.

    Args:
        nums: A list of integers.

    Returns:
        The list shifted left by one element.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> shift_left([6, 2, 5, 3])
        [2, 5, 3, 6]
        >>> shift_left([1, 2])
        [2, 1]
        >>> shift_left([1])
        [1]
    """
    return nums[1:] + nums[:1] if len(nums) > 1 else list(nums)


if __name__ == "__main__":
    print(shift_left([6, 2, 5, 3]))
    print(shift_left([1, 2]))
    print(shift_left([1]))
