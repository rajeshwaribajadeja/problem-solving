"""String-2: xy_balance problem solution."""


def xy_balance(s: str) -> bool:
    """Return True if for all 'x' chars, there is a 'y' later in the string.

    We'll say that a string is xy-balanced if for all the 'x' chars in the
    string, there exists a 'y' char somewhere later in the string. One 'y'
    can balance multiple 'x's. A string without 'x' is balanced by default.

    Args:
        s: The input string.

    Returns:
        True if the string is xy-balanced, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> xy_balance("aaxbby")
        True
        >>> xy_balance("aaxbb")
        False
        >>> xy_balance("yaaxbb")
        False
    """
    return s.rfind("y") >= s.rfind("x")


if __name__ == "__main__":
    print(xy_balance("aaxbby"))
    print(xy_balance("aaxbb"))
    print(xy_balance("yaaxbb"))