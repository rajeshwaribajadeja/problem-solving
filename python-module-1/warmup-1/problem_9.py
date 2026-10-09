"""Warmup-1: not_string problem solution."""


def not_string(s: str) -> str:
    """Add 'not ' to the front of a string unless it already begins with 'not'.

    Given a string, return a new string with 'not ' added to the front.
    If the string already begins with 'not', return the original string
    unchanged.

    Args:
        s: The input string.

    Returns:
        The string prefixed with 'not ', or unchanged if already present.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting string.

    Examples:
        >>> not_string('candy')
        'not candy'
        >>> not_string('x')
        'not x'
        >>> not_string('not bad')
        'not bad'
    """
    return s if s.startswith("not") else f"not {s}"


if __name__ == "__main__":
    print(not_string("candy"))
    print(not_string("x"))
    print(not_string("not bad"))
