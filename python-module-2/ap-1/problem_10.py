"""AP-1: copy_evens problem solution."""


def copy_evens(nums: list, count: int) -> list:
    """Return a new array containing the first 'count' even numbers.

    Given an array of positive ints, return a new array of length "count"
    containing the first even numbers from the original array. The original
    array will contain at least "count" even numbers.

    Args:
        nums: A list of positive integers.
        count: The number of even elements to extract.

    Returns:
        A list of length 'count' containing the first even numbers.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(count) for the result list.

    Examples:
        >>> copy_evens([3, 2, 4, 5, 8], 2)
        [2, 4]
        >>> copy_evens([3, 2, 4, 5, 8], 3)
        [2, 4, 8]
        >>> copy_evens([6, 1, 2, 4, 5, 8], 3)
        [6, 2, 4]
    """
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
            if len(result) == count:
                break
    return result


if __name__ == "__main__":
    print(copy_evens([3, 2, 4, 5, 8], 2))
    print(copy_evens([3, 2, 4, 5, 8], 3))
    print(copy_evens([6, 1, 2, 4, 5, 8], 3))