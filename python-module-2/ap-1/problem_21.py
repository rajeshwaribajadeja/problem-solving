"""AP-1: common_two problem solution."""


def common_two(a: list, b: list) -> int:
    """Return count of unique strings that appear in both sorted arrays.

    Start with two arrays of strings, a and b, each in alphabetical order,
    possibly with duplicates. Return the count of the number of unique
    strings which appear in both arrays.

    Args:
        a: First sorted list of strings.
        b: Second sorted list of strings.

    Returns:
        The count of unique strings present in both lists.

    Complexity:
        Time Complexity: O(len(a) + len(b))
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> common_two(["a", "c", "x"], ["b", "c", "d", "x"])
        2
        >>> common_two(["a", "c", "x"], ["a", "b", "c", "x", "z"])
        3
        >>> common_two(["a", "b", "c"], ["a", "b", "c"])
        3
    """
    
    return len(set(a) & set(b))


if __name__ == "__main__":
    print(common_two(["a", "c", "x"], ["b", "c", "d", "x"]))
    print(common_two(["a", "c", "x"], ["a", "b", "c", "x", "z"]))
    print(common_two(["a", "b", "c"], ["a", "b", "c"]))