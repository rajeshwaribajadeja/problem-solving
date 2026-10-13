"""Array-2: pre_4 problem solution."""


def pre_4(nums: list) -> list:
    """Return array containing elements preceding the first 4.

    Given a non-empty array of ints, return a new array containing the
    elements from the original array that come before the first 4.

    Args:
        nums: A list of integers containing at least one 4.

    Returns:
        The elements preceding the first 4.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> pre_4([1, 2, 4, 1])
        [1, 2]
        >>> pre_4([3, 1, 4])
        [3, 1] 
        >>> pre_4([1, 4, 4])
        [1]
    """
    return nums[:nums.index(4)] if 4 in nums else nums[:]


if __name__ == "__main__":
    print(pre_4([1, 2, 4, 1]))
    print(pre_4([3, 1, 4]))
    print(pre_4([1, 4, 4]))
