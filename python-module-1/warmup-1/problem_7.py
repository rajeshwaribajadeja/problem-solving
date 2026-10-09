"""Warmup-1: near_hundred problem solution."""


def near_hundred(n: int) -> bool:
    """Check if an integer is within 10 of 100 or within 10 of 200.

    Given an int n, return True if it is within 10 of 100 (in the range
    90..110) or within 10 of 200 (in the range 190..210).

    Args:
        n: An integer value.

    Returns:
        True if n is within 10 of 100 or 200, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> near_hundred(93)
        True
        >>> near_hundred(90)
        True
        >>> near_hundred(89)
        False
    """
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


if __name__ == "__main__":
    print(near_hundred(93))
    print(near_hundred(90))
    print(near_hundred(89))