"""Array-2: either_24 problem solution."""


def either_24(nums: list) -> bool:
    """Return True if array contains 2 next to 2 or 4 next to 4, but not both.

    Args:
        nums: A list of integers.

    Returns:
        True if adjacent 2s or adjacent 4s exist (exclusive), False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> either_24([1, 2, 2])
        True
        >>> either_24([4, 4, 1])
        True
        >>> either_24([4, 4, 1, 2, 2])
        False
    """
    has_22 = any(nums[i] == 2 and nums[i + 1] == 2 for i in range(len(nums) - 1))
    has_44 = any(nums[i] == 4 and nums[i + 1] == 4 for i in range(len(nums) - 1))
    return has_22 != has_44


if __name__ == "__main__":
    print(either_24([1, 2, 2]))
    print(either_24([4, 4, 1]))
    print(either_24([4, 4, 1, 2, 2]))
