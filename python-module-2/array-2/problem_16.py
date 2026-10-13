"""Array-2: same_ends problem solution."""


def same_ends(nums: list, n: int) -> bool:
    """Return True if the group of N numbers at start and end match.

    Return True if the group of N numbers at the start and end
    of the array are the same.

    Args:
        nums: A list of integers.
        n: The length of the prefix and suffix to compare.

    Returns:
        True if nums[:n] equals nums[-n:] or n == 0, False otherwise.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)

    Examples:
        >>> same_ends([5, 6, 45, 99, 13, 5, 6], 1)
        False
        >>> same_ends([5, 6, 45, 99, 13, 5, 6], 2)
        True
        >>> same_ends([5, 6, 45, 99, 13, 5, 6], 3)
        False
    """

    return n == 0 or nums[:n] == nums[-n:]


if __name__ == "__main__":
    print(same_ends([5, 6, 45, 99, 13, 5, 6], 1))
    print(same_ends([5, 6, 45, 99, 13, 5, 6], 2))
    print(same_ends([5, 6, 45, 99, 13, 5, 6], 3))
