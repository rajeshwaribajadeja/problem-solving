"""Array-2: post_4 problem solution."""


def post_4(nums: list) -> list:
    """Return array containing elements following the last 4.

    Given a non-empty array of ints, return a new array containing the
    elements from the original array that come after the last 4 in the
    original array. The original array will contain at least one 4.

    Args:
        nums: A list of integers containing at least one 4.

    Returns:
        The elements following the last 4.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> post_4([2, 4, 1, 2])
        [1, 2]
        >>> post_4([4, 1, 4, 2])
        [2]
        >>> post_4([4, 4, 1, 2, 3])
        [1, 2, 3]
    """
    last_4 = len(nums) - 1 - nums[::-1].index(4)
    return nums[last_4 + 1:]


if __name__ == "__main__":
    print(post_4([2, 4, 1, 2]))
    print(post_4([4, 1, 4, 2]))
    print(post_4([4, 4, 1, 2, 3]))
