"""Array-3: linear_in problem solution."""


def linear_in(outer: list, inner: list) -> bool:
    """Return True if all numbers in inner appear in outer.

    Given two arrays of ints sorted in increasing order, outer and inner,
    return True if all of the numbers in inner appear in outer. Makes a
    single linear pass taking advantage of the sorted order.

    Args:
        outer: A sorted list of integers in increasing order.
        inner: A sorted list of integers in increasing order.

    Returns:
        True if all elements of inner are present in outer, False otherwise.

    Complexity:
        Time Complexity: O(N + M) where N = len(outer) and M = len(inner).
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> linear_in([1, 2, 4, 6], [2, 4])
        True
        >>> linear_in([1, 2, 4, 6], [2, 3, 4])
        False
        >>> linear_in([1, 2, 4, 4, 6], [2, 4])
        True
    """
    i = 0
    j = 0

    while i < len(outer) and j < len(inner):
        if outer[i] == inner[j]:
            i += 1
            j += 1
        elif outer[i] < inner[j]:
            i += 1
        else:
            return False

    return j == len(inner)


if __name__ == "__main__":
    print(linear_in([1, 2, 4, 6], [2, 4]))
    print(linear_in([1, 2, 4, 6], [2, 3, 4]))
    print(linear_in([1, 2, 4, 4, 6], [2, 4]))
