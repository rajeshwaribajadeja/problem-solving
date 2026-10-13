"""List-1: rotate_left3 problem solution."""


def rotate_left3(nums: list) -> list:
    """Return an array of length 3 rotated left by one position.

    Given an array of ints length 3, return an array with the elements
    "rotated left" so [1, 2, 3] yields [2, 3, 1].

    Args:
        nums: A list of 3 integers.

    Returns:
        The rotated list of 3 integers.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> rotate_left3([1, 2, 3])
        [2, 3, 1]
        >>> rotate_left3([5, 11, 9])
        [11, 9, 5]
        >>> rotate_left3([7, 0, 0])
        [0, 0, 7]
    """
    return [nums[1], nums[2], nums[0]]


if __name__ == "__main__":
    print(rotate_left3([1, 2, 3]))
    print(rotate_left3([5, 11, 9]))
    print(rotate_left3([7, 0, 0]))
