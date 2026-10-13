"""List-1: common_end problem solution."""


def common_end(a: list, b: list) -> bool:
    """Return True if two lists have the same first or last element.

    Given 2 arrays of ints, a and b, return True if they have the same
    first element or they have the same last element. Both arrays will
    be length 1 or more.

    Args:
        a: First list of integers (length >= 1).
        b: Second list of integers (length >= 1).

    Returns:
        True if first elements match or last elements match, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> common_end([1, 2, 3], [7, 3])
        True
        >>> common_end([1, 2, 3], [7, 3, 2])
        False
        >>> common_end([1, 2, 3], [1, 3])
        True
    """
    return a[0] == b[0] or a[-1] == b[-1]


if __name__ == "__main__":
    print(common_end([1, 2, 3], [7, 3]))
    print(common_end([1, 2, 3], [7, 3, 2]))
    print(common_end([1, 2, 3], [1, 3]))
