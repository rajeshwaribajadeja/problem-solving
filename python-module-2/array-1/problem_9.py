"""Array-1: swap_ends problem solution."""


def swap_ends(nums: list) -> list:
    """Swap the first and last elements in the array.

    Given an array of ints, swap the first and last elements in the array.
    Return the modified array. The array length will be at least 1.

    Args:
        nums: A list of integers (length >= 1).

    Returns:
        The array with first and last elements swapped.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> swap_ends([1, 2, 3, 4])
        [4, 2, 3, 1]
        >>> swap_ends([1, 2, 3])
        [3, 2, 1]
        >>> swap_ends([8, 6, 7, 9, 5])
        [5, 6, 7, 9, 8]
    """
    result = list(nums)
    result[0], result[-1] = result[-1], result[0]
    return result


if __name__ == "__main__":
    print(swap_ends([1, 2, 3, 4]))
    print(swap_ends([1, 2, 3]))
    print(swap_ends([8, 6, 7, 9, 5]))
