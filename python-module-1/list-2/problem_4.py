"""List-2: sum13 problem solution."""


def sum13(nums: list) -> int:
    """Return the sum of numbers in array, ignoring 13 and numbers after it.

    Return the sum of the numbers in the array, returning 0 for an empty
    array. The number 13 is unlucky, so it does not count and numbers
    that come immediately after a 13 also do not count.

    Args:
        nums: A list of integers.

    Returns:
        The computed sum excluding 13 and elements immediately following 13.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> sum13([1, 2, 2, 1])
        6
        >>> sum13([1, 1])
        2
        >>> sum13([1, 2, 2, 1, 13])
        6
    """
    total = 0
    ignore = False

    for num in nums:
        if ignore:
            ignore = False
        elif num == 13:
            ignore = True
        else:
            total += num

    return total


if __name__ == "__main__":
    print(sum13([1, 2, 2, 1]))
    print(sum13([1, 1]))
    print(sum13([1, 2, 2, 1, 13]))