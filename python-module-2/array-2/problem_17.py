"""Array-2: triple_up problem solution."""


def triple_up(nums: list) -> bool:
    """Return True if the array contains three increasing adjacent numbers.

    Args:
        nums: A list of integers.

    Returns:
        True if 3 adjacent values increase by 1, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> triple_up([1, 4, 5, 6, 2])
        True
        >>> triple_up([1, 2, 3])
        True
        >>> triple_up([1, 2, 4])
        False
    """
    return any(b == a+1 and c == b+1 for a, b, c in zip(nums, nums[1:], nums[2:]))


if __name__ == "__main__":
    print(triple_up([1, 4, 5, 6, 2]))
    print(triple_up([1, 2, 3]))
    print(triple_up([1, 2, 4]))
