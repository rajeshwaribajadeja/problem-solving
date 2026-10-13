"""List-2: sum67 problem solution."""


def sum67(nums: list) -> int:
    """Return the sum of numbers in the array, ignoring sections from 6 to 7.

    Return the sum of the numbers in the array, except ignore sections of
    numbers starting with a 6 and extending to the next 7 (every 6 will be
    followed by at least one 7). Return 0 for no numbers.

    Args:
        nums: A list of integers.

    Returns:
        The computed sum ignoring sections bounded by 6 and 7.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> sum67([1, 2, 2])
        5
        >>> sum67([1, 2, 2, 6, 99, 99, 7])
        5
        >>> sum67([1, 1, 6, 7, 2])
        4
    """
    total = 0
    ignore = False

    for num in nums:
        if num == 6:
            ignore = True
        elif num == 7 and ignore:
            ignore = False
        elif not ignore:
            total += num

    return total


if __name__ == "__main__":
    print(sum67([1, 2, 2]))
    print(sum67([1, 2, 2, 6, 99, 99, 7]))
    print(sum67([1, 1, 6, 7, 2]))