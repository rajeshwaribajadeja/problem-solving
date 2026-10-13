"""Array-2: match_up problem solution."""


def match_up(nums1: list, nums2: list) -> int:
    """Return count of pairs differing by 2 or less, but not equal.

    Given arrays nums1 and nums2 of the same length, for every element in
    nums1, consider the corresponding element in nums2 (at the same index).
    Return the count of the number of times that the two elements differ by 2
    or less, but are not equal.

    Args:
        nums1: First list of integers.
        nums2: Second list of integers.

    Returns:
        Number of indices where 0 < abs(nums1[i] - nums2[i]) <= 2.

    Complexity:
        Time Complexity: O(N) where N is the length of the lists.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> match_up([1, 2, 3], [2, 3, 10])
        2
        >>> match_up([1, 2, 3], [2, 3, 5])
        3
        >>> match_up([1, 2, 3], [2, 3, 3])
        2
    """
    return sum(0 < abs(a - b) <= 2 for a, b in zip(nums1, nums2))


if __name__ == "__main__":
    print(match_up([1, 2, 3], [2, 3, 10]))
    print(match_up([1, 2, 3], [2, 3, 5]))
    print(match_up([1, 2, 3], [2, 3, 3]))
