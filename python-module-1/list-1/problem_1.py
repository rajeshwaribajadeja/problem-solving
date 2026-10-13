"""List-1: first_last6 problem solution."""


def first_last6(nums: list) -> bool:
    """Return True if 6 appears as either the first or last element.

    Given an array of ints, return True if 6 appears as either the first or
    last element in the array. The array will be length 1 or more.

    Args:
        nums: A list of integers of length 1 or more.

    Returns:
        True if 6 is the first or last element, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> first_last6([1, 2, 6])
        True
        >>> first_last6([6, 1, 2, 3])
        True
        >>> first_last6([13, 6, 1, 2, 3])
        False
    """
    return nums[0] == 6 or nums[-1] == 6


if __name__ == "__main__":
    print(first_last6([1, 2, 6]))
    print(first_last6([6, 1, 2, 3]))
    print(first_last6([13, 6, 1, 2, 3]))