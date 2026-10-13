"""List-1: has23 problem solution."""


def has23(nums: list) -> bool:
    """Return True if 2 or 3 is in an array of length 2.

    Given an array of ints length 2, return True if 2 or 3 is in the array.

    Args:
        nums: A list of 2 integers.

    Returns:
        True if 2 or 3 is present in the list, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> has23([2, 5])
        True
        >>> has23([4, 3])
        True
        >>> has23([4, 5])
        False
    """
    return 2 in nums or 3 in nums


if __name__ == "__main__":
    print(has23([2, 5]))
    print(has23([4, 3]))
    print(has23([4, 5]))
