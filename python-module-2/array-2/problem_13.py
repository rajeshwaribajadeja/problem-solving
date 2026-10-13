"""Array-2: mod_three problem solution."""


def mod_three(nums: list) -> bool:
    """Return True if array contains 3 even or 3 odd values adjacent.

    Given an array of ints, return True if the array contains either
    3 even or 3 odd values all next to each other.

    Args:
        nums: A list of integers.

    Returns:
        True if 3 consecutive numbers share the same parity, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> mod_three([2, 1, 3, 5])
        True
        >>> mod_three([2, 1, 2, 5])
        False
        >>> mod_three([2, 4, 2, 5])
        True
    """
    return any(nums[i] % 2 == nums[i+1] % 2 == nums[i+2] % 2 for i in range(len(nums)-2))

if __name__ == "__main__":
    print(mod_three([2, 1, 3, 5]))
    print(mod_three([2, 1, 2, 5]))
    print(mod_three([2, 4, 2, 5]))
