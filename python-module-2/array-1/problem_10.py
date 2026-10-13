"""Array-1: mid_three problem solution."""


def mid_three(nums: list) -> list:
    """Return a new array of length 3 containing the middle elements.

    Given an array of ints of odd length, return a new array length 3
    containing the elements from the middle of the array.

    Args:
        nums: A list of integers of odd length (length >= 3).

    Returns:
        A list of length 3 with the central elements of the array.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> mid_three([1, 2, 3, 4, 5])
        [2, 3, 4]
        >>> mid_three([8, 6, 7, 5, 3, 0, 9])
        [7, 5, 3]
        >>> mid_three([1, 2, 3])
        [1, 2, 3]
    """
    middle = len(nums) // 2
    return nums[middle - 1:middle + 2]


if __name__ == "__main__":
    print(mid_three([1, 2, 3, 4, 5]))
    print(mid_three([8, 6, 7, 5, 3, 0, 9]))
    print(mid_three([1, 2, 3]))