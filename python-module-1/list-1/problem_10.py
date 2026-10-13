"""List-1: middle_way problem solution."""


def middle_way(a: list, b: list) -> list:
    """Create a new array of length 2 containing their middle elements.

    Given 2 int arrays, a and b, each length 3, create a new array
    of length 2 containing their middle elements.

    Args:
        a: First list of 3 integers.
        b: Second list of 3 integers.

    Returns:
        A list of length 2 containing the middle elements [a[1], b[1]].

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> middle_way([1, 2, 3], [4, 5, 6])
        [2, 5]
        >>> middle_way([7, 7, 7], [3, 8, 0])
        [7, 8]
        >>> middle_way([5, 2, 9], [1, 4, 5])
        [2, 4]
    """
    return [a[1], b[1]]


if __name__ == "__main__":
    print(middle_way([1, 2, 3], [4, 5, 6]))
    print(middle_way([7, 7, 7], [3, 8, 0]))
    print(middle_way([5, 2, 9], [1, 4, 5]))
