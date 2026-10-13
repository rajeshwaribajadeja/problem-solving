"""List-2: has22 problem solution."""


def has22(nums: list) -> bool:
    """Return True if the array contains a 2 next to a 2 somewhere.

    Given an array of ints, return True if the array contains a 2 next
    to a 2 somewhere.

    Args:
        nums: A list of integers.

    Returns:
        True if the list contains adjacent 2s, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> has22([1, 2, 2])
        True
        >>> has22([1, 2, 1, 2])
        False
        >>> has22([2, 1, 2])
        False
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


if __name__ == "__main__":
    print(has22([1, 2, 2]))
    print(has22([1, 2, 1, 2]))
    print(has22([2, 1, 2]))