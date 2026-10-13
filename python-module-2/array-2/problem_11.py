"""Array-2: has_77 problem solution."""


def has_77(nums: list) -> bool:
    """Return True if the array contains two 7s adjacent or separated by one.

    Given an array of ints, return True if the array contains two 7's
    next to each other, or there are two 7's separated by one element.

    Args:
        nums: A list of integers.

    Returns:
        True if 7s appear with gap <= 1, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> has_77([1, 7, 7])
        True
        >>> has_77([1, 7, 1, 7])
        True
        >>> has_77([1, 7, 1, 1, 7])
        False
    """
    return any(nums[i] == 7 and 7 in nums[i+1:i+3] for i in range(len(nums)-1))


if __name__ == "__main__":
    print(has_77([1, 7, 7]))
    print(has_77([1, 7, 1, 7]))
    print(has_77([1, 7, 1, 1, 7]))
