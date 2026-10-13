"""List-2: count_evens problem solution."""


def count_evens(nums: list) -> int:
    """Return the number of even ints in the given array.

    Args:
        nums: A list of integers.

    Returns:
        The count of even integers.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> count_evens([2, 1, 2, 3, 4])
        3
        >>> count_evens([2, 2, 0])
        3
        >>> count_evens([1, 3, 5])
        0
    """
    return sum(1 for n in nums if n % 2 == 0)


if __name__ == "__main__":
    print(count_evens([2, 1, 2, 3, 4]))
    print(count_evens([2, 2, 0]))
    print(count_evens([1, 3, 5]))
