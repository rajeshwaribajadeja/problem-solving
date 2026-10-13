"""List-1: max_end3 problem solution."""


def max_end3(nums: list) -> list:
    """Return an array with all elements set to the larger of first or last.

    Given an array of ints length 3, figure out which is larger, the first
    or the last. Return a new array of length 3 containing this "largest"
    value at each of the 3 positions.

    Args:
        nums: A list of 3 integers.

    Returns:
        A list of length 3 filled with the larger of the first and last elements.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> max_end3([1, 2, 3])
        [3, 3, 3]
        >>> max_end3([11, 5, 9])
        [11, 11, 11]
        >>> max_end3([2, 11, 3])
        [3, 3, 3]
    """
    return [max(nums[0], nums[-1])] * 3


if __name__ == "__main__":
    print(max_end3([1, 2, 3]))
    print(max_end3([11, 5, 9]))
    print(max_end3([2, 11, 3]))
