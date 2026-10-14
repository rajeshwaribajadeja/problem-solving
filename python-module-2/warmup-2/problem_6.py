"""Warmup-2: array667 problem solution."""


def array667(nums: list) -> int:
    """Return count of adjacent pairs of 6 followed by 6 or 7.

    Args:
        nums: List of integers.

    Returns:
        Number of occurrences of 6 followed by 6 or 7.

    Complexity:
        Time Complexity: O(n) where n is len(nums).
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> array667([6, 6, 2])
        1
        >>> array667([6, 6, 2, 6])
        1
        >>> array667([6, 7, 2, 6])
        1
    """
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] == 6 and nums[i + 1] in (6, 7):
            count += 1
    return count


if __name__ == "__main__":
    print(array667([6, 6, 2]))
    print(array667([6, 6, 2, 6]))
    print(array667([6, 7, 2, 6]))