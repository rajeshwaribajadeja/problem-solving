"""List-1: sum3 problem solution."""


def sum3(nums: list) -> int:
    """Return the sum of all elements in an integer array of length 3.

    Args:
        nums: A list of 3 integers.

    Returns:
        The sum of the 3 integers.

    Complexity:
        Time Complexity: O(N)
        Space Complexity: O(1)

    Examples:
        >>> sum3([1, 2, 3])
        6
        >>> sum3([5, 11, 2])
        18
        >>> sum3([7, 0, 0])
        7
    """
    return sum(nums)


if __name__ == "__main__":
    print(sum3([1, 2, 3]))
    print(sum3([5, 11, 2]))
    print(sum3([7, 0, 0]))
