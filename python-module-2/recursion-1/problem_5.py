"""Recursion-1: triangle problem solution."""


def triangle(rows: int) -> int:
    """Return total number of blocks in a triangle with the given rows.

    Args:
        rows: Number of rows in the triangle.

    Returns:
        Total blocks in the triangle.

    Complexity:
        Time Complexity: O(rows) recursive calls.
        Space Complexity: O(rows) auxiliary space for the call stack.

    Examples:
        >>> triangle(0)
        0
        >>> triangle(1)
        1
        >>> triangle(2)
        3
    """
    
    return 0 if rows <= 0 else rows + triangle(rows - 1)


if __name__ == "__main__":
    print(triangle(0))
    print(triangle(1))
    print(triangle(2))
