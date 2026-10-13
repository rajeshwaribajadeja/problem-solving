"""Array-1: make_last problem solution."""


def make_last(nums: list) -> list:
    """Return a new array of double length ending with the original last element.

    Given an int array, return a new array with double the length where
    its last element is the same as the original array, and all the other
    elements are 0.

    Args:
        nums: A list of integers.

    Returns:
        A list of length 2 * len(nums) with 0s except the final element.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) for the new doubled-length list.

    Examples:
        >>> make_last([4, 5, 6])
        [0, 0, 0, 0, 0, 6]
        >>> make_last([1, 2])
        [0, 0, 0, 2]
        >>> make_last([3])
        [0, 3]
    """
    return [0] * (len(nums) * 2 - 1) + nums[-1:]


if __name__ == "__main__":
    print(make_last([4, 5, 6]))
    print(make_last([1, 2]))
    print(make_last([3]))
