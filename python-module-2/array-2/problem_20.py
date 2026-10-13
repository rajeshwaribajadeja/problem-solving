"""Array-2: ten_run problem solution."""


def ten_run(nums: list) -> list:
    """Fill elements following each multiple of 10 with that multiple.

    For each multiple of 10 in the given array, change all values following
    it to be that multiple of 10, until encountering another multiple of 10.

    Args:
        nums: A list of integers.

    Returns:
        The updated list following the ten-run rule.

    Complexity:
        Time Complexity: O(N) where N is the length of the list.
        Space Complexity: O(N) auxiliary space.

    Examples:
        >>> ten_run([2, 10, 3, 4, 20, 5])
        [2, 10, 10, 10, 20, 20]
        >>> ten_run([10, 1, 20, 2])
        [10, 10, 20, 20]
        >>> ten_run([10, 1, 9, 20])
        [10, 10, 10, 20]
    """
    current = None
    result = []
    for n in nums:
        current = n if n % 10 == 0 else current
        result.append(current if current is not None else n)
    return result


if __name__ == "__main__":
    print(ten_run([2, 10, 3, 4, 20, 5]))
    print(ten_run([10, 1, 20, 2]))
    print(ten_run([10, 1, 9, 20]))
