"""List-1: same_first_last problem solution."""


def same_first_last(nums: list) -> bool:
    """Return True if the list is non-empty and first and last elements match.

    Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal.

    Args:
        nums: A list of integers.

    Returns:
        True if length >= 1 and first equals last element, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> same_first_last([1, 2, 3])
        False
        >>> same_first_last([1, 2, 3, 1])
        True
        >>> same_first_last([1, 2, 1])
        True
    """
    return len(nums) >= 1 and nums[0] == nums[-1]


if __name__ == "__main__":
    print(same_first_last([1, 2, 3]))
    print(same_first_last([1, 2, 3, 1]))
    print(same_first_last([1, 2, 1]))