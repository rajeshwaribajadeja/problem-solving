"""Array-2: is_everywhere problem solution."""


def is_everywhere(nums: list, val: int) -> bool:
    """Return True if val is in every adjacent pair of elements.

    We'll say that a value is "everywhere" in an array if for every pair
    of adjacent elements in the array, at least one of the pair is that value.

    Args:
        nums: A list of integers.
        val: The target integer to check.

    Returns:
        True if val appears in every adjacent pair, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> is_everywhere([1, 2, 1, 3], 1)
        True
        >>> is_everywhere([1, 2, 1, 3], 2)
        False
        >>> is_everywhere([1, 2, 1, 3, 4], 1)
        False
    """
    for i in range(len(nums) - 1):
        if nums[i] != val and nums[i + 1] != val:
            return False
    return True


if __name__ == "__main__":
    print(is_everywhere([1, 2, 1, 3], 1))
    print(is_everywhere([1, 2, 1, 3], 2))
    print(is_everywhere([1, 2, 1, 3, 4], 1))
