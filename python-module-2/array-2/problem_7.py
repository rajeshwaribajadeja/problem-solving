"""Array-2: no_14 problem solution."""


def no_14(nums: list) -> bool:
    """Return True if the array contains no 1s or contains no 4s.

    Given an array of ints, return True if it contains no 1's
    or it contains no 4's.

    Args:
        nums: A list of integers.

    Returns:
        True if 1 is absent or 4 is absent, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> no_14([1, 2, 3])
        True
        >>> no_14([1, 2, 3, 4])
        False
        >>> no_14([2, 3, 4])
        True
    """
    return 1 not in nums or 4 not in nums


if __name__ == "__main__":
    print(no_14([1, 2, 3]))
    print(no_14([1, 2, 3, 4]))
    print(no_14([2, 3, 4]))
