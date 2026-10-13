"""Array-1: no23 problem solution."""


def no23(nums: list) -> bool:
    """Return True if the array does not contain a 2 or 3.

    Given an int array length 2, return True if it does not contain a 2 or 3.

    Args:
        nums: A list of 2 integers.

    Returns:
        True if neither 2 nor 3 is present in the array, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> no23([4, 5])
        True
        >>> no23([4, 2])
        False
        >>> no23([3, 5])
        False
    """
    return 2 not in nums and 3 not in nums


if __name__ == "__main__":
    print(no23([4, 5]))
    print(no23([4, 2]))
    print(no23([3, 5]))
