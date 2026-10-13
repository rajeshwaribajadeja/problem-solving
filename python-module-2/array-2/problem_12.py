"""Array-2: has_12 problem solution."""


def has_12(nums: list) -> bool:
    """Return True if there is a 1 in the array followed by a 2 later.

    Given an array of ints, return True if there is a 1 in the array
    with a 2 somewhere later in the array.

    Args:
        nums: A list of integers.

    Returns:
        True if a 1 appears before a 2 in the list, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> has_12([1, 3, 2])
        True
        >>> has_12([3, 1, 2])
        True
        >>> has_12([3, 1, 4, 5, 2])
        True
    """
    found_1 = False
    for num in nums:
        if num == 1:
            found_1 = True
        elif num == 2 and found_1:
            return True
    return False


if __name__ == "__main__":
    print(has_12([1, 3, 2]))
    print(has_12([3, 1, 2]))
    print(has_12([3, 1, 4, 5, 2]))
