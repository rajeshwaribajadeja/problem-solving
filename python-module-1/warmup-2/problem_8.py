"""Warmup-2: array123 problem solution."""


def array123(nums: list[int]) -> bool:
    """Return True if the sequence of numbers 1, 2, 3 appears in the array.

    Given an array of ints, return True if the sequence of numbers
    1, 2, 3 appears anywhere in the array.

    Args:
        nums: A list of integers.

    Returns:
        True if the subsequence [1, 2, 3] appears in nums, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of nums.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> array123([1, 1, 2, 3, 1])
        True
        >>> array123([1, 1, 2, 4, 1])
        False
        >>> array123([1, 1, 2, 1, 2, 3])
        True
    """
    return any(
        nums[start_index : start_index + 3] == [1, 2, 3]
        for start_index in range(len(nums) - 2)
    )


if __name__ == "__main__":
    print(array123([1, 1, 2, 3, 1]))
    print(array123([1, 1, 2, 4, 1]))
    print(array123([1, 1, 2, 1, 2, 3]))
