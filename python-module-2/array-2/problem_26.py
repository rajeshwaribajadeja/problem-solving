"""Array-2: zero_max problem solution."""


def zero_max(nums: list) -> list:
    """Replace each 0 with the largest odd value to its right.

    Return a version of the given array where each zero value in the array
    is replaced by the largest odd value to the right of the zero.
    If there is no odd value to the right of the zero, leave it as zero.

    Args:
        nums: A list of integers.

    Returns:
        The list with zeros replaced by the maximum odd number to the right.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> zero_max([0, 5, 0, 3])
        [5, 5, 3, 3]
        >>> zero_max([0, 4, 0, 3])
        [3, 4, 3, 3]
        >>> zero_max([0, 1, 0])
        [1, 1, 0]
    """
    result = nums.copy()
    max_odd = 0

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            result[i] = max_odd
        elif nums[i] % 2:
            max_odd = max(max_odd, nums[i])

    return result


if __name__ == "__main__":
    print(zero_max([0, 5, 0, 3]))
    print(zero_max([0, 4, 0, 3]))
    print(zero_max([0, 1, 0]))
