"""Array-2: two_two problem solution."""


def two_two(nums: list) -> bool:
    """Return True if every 2 in the array is adjacent to another 2.

    Given an array of ints, return True if every 2 that appears
    in the array is next to another 2.

    Args:
        nums: A list of integers.

    Returns:
        True if all 2s are part of a run of at least two 2s,
        False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> two_two([4, 2, 2, 3])
        True
        >>> two_two([2, 2, 4])
        True
        >>> two_two([2, 2, 4, 2])
        False
    """
    return all(
        (i > 0 and nums[i - 1] == 2)
        or (i < len(nums) - 1 and nums[i + 1] == 2)
        for i in range(len(nums))
        if nums[i] == 2
    )


if __name__ == "__main__":
    print(two_two([4, 2, 2, 3]))
    print(two_two([2, 2, 4]))
    print(two_two([2, 2, 4, 2]))
