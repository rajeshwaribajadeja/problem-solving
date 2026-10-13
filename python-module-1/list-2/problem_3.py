"""List-2: centered_average problem solution."""


def centered_average(nums: list) -> int:
    """Return the centered average of an array of ints using integer division.

    Return the "centered" average of an array of ints, which we'll say is the
    mean average of the values, except ignoring the largest and smallest values
    in the array. If there are multiple copies of the smallest value, ignore
    just one copy, and likewise for the largest value. Use int division to
    produce the final average. You may assume that the array is length 3 or more.

    Args:
        nums: A list of integers (length >= 3).

    Returns:
        The centered average calculated using integer division.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> centered_average([1, 2, 3, 4, 100])
        3
        >>> centered_average([1, 1, 5, 5, 10, 8, 7])
        5
        >>> centered_average([-10, -4, -2, -4, -2, 0])
        -3
    """
    total = sum(nums) - min(nums) - max(nums)
    return total // (len(nums) - 2)


if __name__ == "__main__":
    print(centered_average([1, 2, 3, 4, 100]))
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))
    print(centered_average([-10, -4, -2, -4, -2, 0]))