"""Array-2: only_14 problem solution."""


def only_14(nums: list) -> bool:
    """Return True if every element in the array is a 1 or a 4.

    Args:
        nums: A list of integers.

    Returns:
        True if all elements are 1 or 4, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> only_14([1, 4, 1, 4])
        True
        >>> only_14([1, 4, 2, 4])
        False
        >>> only_14([1, 1])
        True
    """
    return all(num == 1 or num == 4 for num in nums)


if __name__ == "__main__":
    print(only_14([1, 4, 1, 4]))
    print(only_14([1, 4, 2, 4]))
    print(only_14([1, 1]))