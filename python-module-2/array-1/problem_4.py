"""Array-1: fix23 problem solution."""


def fix23(nums: list) -> list:
    """Set the 3 to 0 if a 2 is immediately followed by a 3.

    Given an int array length 3, if there is a 2 in the array immediately
    followed by a 3, set the 3 element to 0. Return the changed array.

    Args:
        nums: A list of 3 integers.

    Returns:
        The updated list with 3 replaced by 0 after a 2.

    Complexity:
        Time Complexity: O(N)
        Space Complexity: O(N)

    Examples:
        >>> fix23([1, 2, 3])
        [1, 2, 0]
        >>> fix23([2, 3, 5])
        [2, 0, 5]
        >>> fix23([1, 2, 1])
        [1, 2, 1]
    """
    return [
        0 if i > 0 and nums[i - 1] == 2 and nums[i] == 3 else nums[i]
        for i in range(len(nums))
    ]


if __name__ == "__main__":
    print(fix23([1, 2, 3]))
    print(fix23([2, 3, 5]))
    print(fix23([1, 2, 1]))
