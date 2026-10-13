"""Array-2: even_odd problem solution."""


def even_odd(nums: list) -> list:
    """Rearrange the array so even numbers come before odd numbers.

    Return an array that contains the exact same numbers as the given
    array, but rearranged so that all the even numbers come before all
    the odd numbers.

    Args:
        nums: A list of integers.

    Returns:
        The list with all even numbers followed by all odd numbers.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> even_odd([1, 0, 1, 0, 0, 1, 1])
        [0, 0, 0, 1, 1, 1, 1]
        >>> even_odd([3, 3, 2])
        [2, 3, 3]
        >>> even_odd([2, 2, 2])
        [2, 2, 2]
    """
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return evens + odds


if __name__ == "__main__":
    print(even_odd([1, 0, 1, 0, 0, 1, 1]))
    print(even_odd([3, 3, 2]))
    print(even_odd([2, 2, 2]))
