"""Array-3: fix_34 problem solution."""


def fix_34(nums: list) -> list:
    """Rearrange the array so that every 3 is immediately followed by a 4.

    Do not move the 3's, but every other number may move. The array contains
    the same number of 3's and 4's, every 3 has a number after it that is not
    a 3, and a 3 appears in the array before any 4.

    Args:
        nums: A list of integers.

    Returns:
        The rearranged list where every 3 is followed by a 4.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> fix_34([1, 3, 1, 4])
        [1, 3, 4, 1]
        >>> fix_34([1, 3, 1, 4, 4, 3, 1])
        [1, 3, 4, 1, 1, 3, 4]
        >>> fix_34([3, 2, 2, 4])
        [3, 4, 2, 2]
    """
    nums = nums.copy()
    j = 0
    for i, x in enumerate(nums):
        if x == 3:
            while nums[j] != 4:
                j += 1
            nums[i+1], nums[j] = nums[j], nums[i+1]
            j += 1
    return nums


if __name__ == "__main__":
    print(fix_34([1, 3, 1, 4]))
    print(fix_34([1, 3, 1, 4, 4, 3, 1]))
    print(fix_34([3, 2, 2, 4]))