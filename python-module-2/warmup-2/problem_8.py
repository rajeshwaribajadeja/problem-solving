"""Warmup-2: has271 problem solution."""


def has271(nums: list) -> bool:
    """Return True if nums contains a 2, 7, 1 pattern with tolerance.

    A 2, 7, 1 pattern is a value, followed by value + 5, followed by
    value - 1, where the third value can differ by 2 or less from
    value - 1.

    Args:
        nums: List of integers.

    Returns:
        True if the 271 pattern is found, False otherwise.

    Complexity:
        Time Complexity: O(n) where n is len(nums).
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> has271([1, 2, 7, 1])
        True
        >>> has271([1, 2, 8, 1])
        False
        >>> has271([2, 7, 1])
        True
    """
    for i in range(len(nums) - 2):
        val = nums[i]
        if nums[i + 1] == val + 5 and abs(nums[i + 2] - (val - 1)) <= 2:
            return True
    return False


if __name__ == "__main__":
    print(has271([1, 2, 7, 1]))
    print(has271([1, 2, 8, 1]))
    print(has271([2, 7, 1]))