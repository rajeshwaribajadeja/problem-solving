"""Array-2: have_three problem solution."""


def have_three(nums: list) -> bool:
    """Return True if 3 appears exactly 3 times and none are adjacent.

    Given an array of ints, return True if the value 3 appears in the array
    exactly 3 times, and no 3's are next to each other.

    Args:
        nums: A list of integers.

    Returns:
        True if 3 appears 3 times with no adjacent 3s, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> have_three([3, 1, 3, 1, 3])
        True
        >>> have_three([3, 1, 3, 3])
        False
        >>> have_three([3, 4, 3, 3, 4])
        False
    """
    return (
        nums.count(3) == 3
        and not any(a == b == 3 for a, b in zip(nums, nums[1:]))
    )


if __name__ == "__main__":
    print(have_three([3, 1, 3, 1, 3]))
    print(have_three([3, 1, 3, 3]))
    print(have_three([3, 4, 3, 3, 4]))
