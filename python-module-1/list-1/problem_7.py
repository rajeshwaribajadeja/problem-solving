"""List-1: reverse3 problem solution."""


def reverse3(nums: list) -> list:
    """Return an array of length 3 with the elements in reverse order.

    Args:
        nums: A list of 3 integers.

    Returns:
        The reversed list of 3 integers.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> reverse3([1, 2, 3])
        [3, 2, 1]
        >>> reverse3([5, 11, 9])
        [9, 11, 5]
        >>> reverse3([7, 0, 0])
        [0, 0, 7]
    """
    return nums[::-1]


if __name__ == "__main__":
    print(reverse3([1, 2, 3]))
    print(reverse3([5, 11, 9]))
    print(reverse3([7, 0, 0]))
