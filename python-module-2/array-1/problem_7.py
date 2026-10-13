"""Array-1: make_middle problem solution."""


def make_middle(nums: list) -> list:
    """Return a new array of length 2 containing the middle two elements.

    Given an array of ints of even length, return a new array length 2
    containing the middle two elements from the original array.

    Args:
        nums: A list of integers of even length (length >= 2).

    Returns:
        A list of length 2 containing the two central elements.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> make_middle([1, 2, 3, 4])
        [2, 3]
        >>> make_middle([7, 1, 2, 3, 4, 9])
        [2, 3]
        >>> make_middle([1, 2])
        [1, 2]
    """
    middle = len(nums) // 2
    return [nums[middle - 1], nums[middle]]


if __name__ == "__main__":
    print(make_middle([1, 2, 3, 4]))
    print(make_middle([7, 1, 2, 3, 4, 9]))
    print(make_middle([1, 2]))
