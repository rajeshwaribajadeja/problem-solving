"""Array-2: zero_front problem solution."""


def zero_front(nums: list) -> list:
    """Rearrange the array so all zeros are grouped at the start.

    Return an array that contains the exact same numbers as the given
    array, but rearranged so that all the zeros are grouped at the start
    of the array. The order of the non-zero numbers does not matter.

    Args:
        nums: A list of integers.

    Returns:
        The list with all zeros grouped at the front.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> zero_front([1, 0, 0, 1])
        [0, 0, 1, 1]
        >>> zero_front([0, 1, 1, 0, 1])
        [0, 0, 1, 1, 1]
        >>> zero_front([1, 0])
        [0, 1]
    """
    return [x for x in nums if x == 0] + [x for x in nums if x != 0]


if __name__ == "__main__":
    print(zero_front([1, 0, 0, 1]))
    print(zero_front([0, 1, 1, 0, 1]))
    print(zero_front([1, 0]))
