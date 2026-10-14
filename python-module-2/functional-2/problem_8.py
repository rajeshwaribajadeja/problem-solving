"""Functional-2: two_2 problem solution."""


def two_2(nums: list) -> list:
    """Return a list of non-negative integers doubled, omitting any
    ending in 2.

    Args:
        nums: List of non-negative integers.

    Returns:
        List of doubled integers that do not end in 2.

    Complexity:
        Time Complexity: O(n) where n is the number of elements in nums.
        Space Complexity: O(n) for the newly created output list.

    Examples:
        >>> two_2([1, 2, 3])
        [4, 6]
        >>> two_2([2, 6, 11])
        [4]
        >>> two_2([0])
        [0]
    """

    nums = list(map(lambda x: x * 2, nums))

    return list(filter(lambda x: x % 10 != 2, nums))

if __name__ == "__main__":
    print(two_2([1, 2, 3]))
    print(two_2([2, 6, 11]))
    print(two_2([0]))

