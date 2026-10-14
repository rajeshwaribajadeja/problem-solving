"""Array-1: unlucky1 problem solution."""


def unlucky1(nums: list) -> bool:
    """Return True if an unlucky 1 is in the first 2 or last 2 positions.

    We'll say that a 1 immediately followed by a 3 in an array is
    an "unlucky" 1. Return True if the given array contains an unlucky 1
    in the first 2 or last 2 positions in the array.

    Args:
        nums: A list of integers.

    Returns:
        True if [1, 3] appears in the first 2 or last 2 positions,
        False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> unlucky1([1, 3, 4, 5])
        True
        >>> unlucky1([2, 1, 3, 4, 5])
        True
        >>> unlucky1([1, 1, 1])
        False
    """
    if len(nums) < 2:
        return False
    if nums[:2] == [1, 3] or nums[-2:] == [1, 3]:
        return True
    if len(nums) >= 3 and nums[1:3] == [1, 3]:
        return True
    return False


if __name__ == "__main__":
    print(unlucky1([1, 3, 4, 5]))
    print(unlucky1([2, 1, 3, 4, 5]))
    print(unlucky1([1, 1, 1]))
