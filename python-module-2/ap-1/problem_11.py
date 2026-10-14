"""AP-1: copy_endy problem solution."""


def is_endy(n: int) -> bool:
    """Return True if positive integer n is in 0..10 or 90..100.

    Args:
        n: A positive integer.

    Returns:
        True if n is endy, False otherwise.
    """
    return 0 <= n <= 10 or 90 <= n <= 100


def copy_endy(nums: list, count: int) -> list:
    """Return a new array containing the first 'count' endy numbers.

    We'll say that a positive int n is "endy" if it is in the range 0..10
    or 90..100 (inclusive). Given an array of positive ints, return a new
    array of length "count" containing the first endy numbers.

    Args:
        nums: A list of positive integers.
        count: The number of endy elements to extract.

    Returns:
        A list of length 'count' containing the first endy numbers.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(count) for the result list.

    Examples:
        >>> copy_endy([9, 11, 90, 22, 6], 2)
        [9, 90]
        >>> copy_endy([9, 11, 90, 22, 6], 3)
        [9, 90, 6]
        >>> copy_endy([12, 1, 1, 13, 0, 20], 2)
        [1, 1]
    """
    result = []
    for num in nums:
        if is_endy(num):
            result.append(num)
            if len(result) == count:
                break
    return result


if __name__ == "__main__":
    print(copy_endy([9, 11, 90, 22, 6], 2))
    print(copy_endy([9, 11, 90, 22, 6], 3))
    print(copy_endy([12, 1, 1, 13, 0, 20], 2))