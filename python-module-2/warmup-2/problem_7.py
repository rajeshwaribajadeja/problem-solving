"""Warmup-2: no_triples problem solution."""


def no_triples(nums: list) -> bool:
    """Return True if the array does not contain three identical
    consecutive values.

    Args:
        nums: List of integers.

    Returns:
        True if no value appears 3 times in a row, False otherwise.

    Complexity:
        Time Complexity: O(n) where n is len(nums).
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> no_triples([1, 1, 2, 2, 1])
        True
        >>> no_triples([1, 1, 2, 2, 2, 1])
        False
        >>> no_triples([1, 1, 1, 2, 2, 2, 1])
        False
    """
    for i in range(len(nums) - 2):
        if nums[i] == nums[i + 1] == nums[i + 2]:
            return False
    return True


if __name__ == "__main__":
    print(no_triples([1, 1, 2, 2, 1]))
    print(no_triples([1, 1, 2, 2, 2, 1]))
    print(no_triples([1, 1, 1, 2, 2, 2, 1]))