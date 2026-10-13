"""List-1: make_ends problem solution."""


def make_ends(nums: list) -> list:
    """Return a new array of length 2 containing first and last elements.

    Given an array of ints, return a new array length 2 containing the first
    and last elements from the original array. The original array will be
    length 1 or more.

    Args:
        nums: A list of integers (length >= 1).

    Returns:
        A list of length 2 containing [nums[0], nums[-1]].

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> make_ends([1, 2, 3])
        [1, 3]
        >>> make_ends([1, 2, 3, 4])
        [1, 4]
        >>> make_ends([7, 4, 6, 2])
        [7, 2]
    """
    return [nums[0], nums[-1]]


if __name__ == "__main__":
    print(make_ends([1, 2, 3]))
    print(make_ends([1, 2, 3, 4]))
    print(make_ends([7, 4, 6, 2]))