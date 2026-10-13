"""Array-3: max_mirror problem solution."""


def max_mirror(nums: list) -> int:
    """Return the size of the largest mirror section found in the array.

    A "mirror" section in an array is a group of contiguous elements
    such that somewhere in the array, the same group appears in reverse order.

    Args:
        nums: A list of integers.

    Returns:
        The size of the largest mirror section.

    Complexity:
        Time Complexity: O(N^2) where N is the length of the list.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> max_mirror([1, 2, 3, 8, 9, 3, 2, 1])
        3
        >>> max_mirror([1, 2, 1, 4])
        3
        >>> max_mirror([7, 1, 2, 9, 7, 2, 1])
        2
    """
    max_length = 0
    n = len(nums)

    for i in range(n):
        for j in range(n - 1, -1, -1):
            length = 0
            while (
                i + length < n
                and j - length >= 0
                and nums[i + length] == nums[j - length]
            ):
                length += 1

            if length > max_length:
                max_length = length

    return max_length


if __name__ == "__main__":
    print(max_mirror([1, 2, 3, 8, 9, 3, 2, 1]))
    print(max_mirror([1, 2, 1, 4]))
    print(max_mirror([7, 1, 2, 9, 7, 2, 1]))
