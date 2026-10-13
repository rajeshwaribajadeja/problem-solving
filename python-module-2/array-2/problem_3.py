"""Array-2: more14 problem solution."""


def more14(nums: list) -> bool:
    """Return True if the number of 1s is greater than the number of 4s.

    Given an array of ints, return True if the number of 1's
    is greater than the number of 4's.

    Args:
        nums: A list of integers.

    Returns:
        True if count of 1s exceeds count of 4s, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> more14([1, 4, 1])
        True
        >>> more14([1, 4, 1, 4])
        False
        >>> more14([1, 1])
        True
    """
    return nums.count(1) > nums.count(4)


if __name__ == "__main__":
    print(more14([1, 4, 1]))
    print(more14([1, 4, 1, 4]))
    print(more14([1, 1]))
