"""Array-1: max_triple problem solution."""


def max_triple(nums: list) -> int:
    """Return the largest of the first, last, and middle values.

    Given an array of ints of odd length, look at the first, last,
    and middle values in the array and return the largest.

    Args:
        nums: A list of integers of odd length (length >= 1).

    Returns:
        The maximum of the first, middle, and last elements.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> max_triple([1, 2, 3])
        3
        >>> max_triple([1, 5, 3])
        5
        >>> max_triple([5, 2, 3])
        5
    """
    middle = len(nums) // 2
    return max(nums[0], nums[middle], nums[-1])


if __name__ == "__main__":
    print(max_triple([1, 2, 3]))
    print(max_triple([1, 5, 3]))
    print(max_triple([5, 2, 3]))
