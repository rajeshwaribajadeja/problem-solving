"""Array-3: count_clumps problem solution."""


def count_clumps(nums: list) -> int:
    """Return the number of clumps in the given array.

    A "clump" in an array is a series of 2 or more adjacent elements of
    the same value.

    Args:
        nums: A list of integers.

    Returns:
        The count of clumps in the array.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> count_clumps([1, 2, 2, 3, 4, 4])
        2
        >>> count_clumps([1, 1, 2, 1, 1])
        2
        >>> count_clumps([1, 1, 1, 1, 1])
        1
    """
    count = 0
    i = 0
    n = len(nums)

    while i < n - 1:
        if nums[i] == nums[i + 1]:
            count += 1
            while i < n - 1 and nums[i] == nums[i + 1]:
                i += 1
        i += 1

    return count


if __name__ == "__main__":
    print(count_clumps([1, 2, 2, 3, 4, 4]))
    print(count_clumps([1, 1, 2, 1, 1]))
    print(count_clumps([1, 1, 1, 1, 1]))
