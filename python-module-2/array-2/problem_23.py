"""Array-2: not_alone problem solution."""


def not_alone(nums: list, val: int) -> list:
    """Replace alone instances of val with the larger of its neighbors.

    We'll say that an element in an array is "alone" if there are values
    before and after it, and those values are different from it. Return
    a version of the given array where every instance of the given value
    which is alone is replaced by whichever value to its left or right
    is larger.

    Args:
        nums: A list of integers.
        val: The target integer to check and potentially replace.

    Returns:
        The modified array with alone values replaced.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> not_alone([1, 2, 3], 2)
        [1, 3, 3]
        >>> not_alone([1, 2, 3, 2, 5, 2], 2)
        [1, 3, 3, 5, 5, 2]
        >>> not_alone([3, 4], 3)
        [3, 4]
    """
    result = list(nums)
    for i in range(1, len(nums) - 1):
        if result[i] == val and result[i - 1] != val and result[i + 1] != val:
            result[i] = max(result[i - 1], result[i + 1])
    return result


if __name__ == "__main__":
    print(not_alone([1, 2, 3], 2))
    print(not_alone([1, 2, 3, 2, 5, 2], 2))
    print(not_alone([3, 4], 3))
