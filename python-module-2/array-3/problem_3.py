"""Array-3: fix_45 problem solution."""


def fix_45(nums: list) -> list:
    """Rearrange the array so that every 4 is immediately followed by a 5.

    Do not move the 4's, but every other number may move. The array contains
    the same number of 4's and 5's, and every 4 has a number after it
    that is not a 4. In this version, 5's may appear anywhere in the
    original array.

    Args:
        nums: A list of integers.

    Returns:
        The rearranged list where every 4 is followed by a 5.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> fix_45([5, 4, 9, 4, 9, 5])
        [9, 4, 5, 4, 5, 9]
        >>> fix_45([1, 4, 1, 5])
        [1, 4, 5, 1]
        >>> fix_45([1, 4, 1, 5, 5, 4, 1])
        [1, 4, 5, 1, 1, 4, 5]
    """
    nums = nums.copy()
    j = 0
    for i, x in enumerate(nums):
        if x == 4:
            while nums[j] != 5 or (j > 0 and nums[j-1] == 4):
                j += 1
            nums[i+1], nums[j] = nums[j], nums[i+1]
    return nums


if __name__ == "__main__":
    print(fix_45([5, 4, 9, 4, 9, 5]))
    print(fix_45([1, 4, 1, 5]))
    print(fix_45([1, 4, 1, 5, 5, 4, 1]))
