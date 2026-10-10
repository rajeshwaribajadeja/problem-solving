"""Warmup-1: start_hi problem solution."""


def start_hi(s: str) -> bool:
    """Return True if the given string starts with 'hi'.

    Given a string, return True if the string starts with "hi" and
    False otherwise.

    Args:
        s: The input string.

    Returns:
        True if the string begins with "hi", False otherwise.

    Complexity:
        Time Complexity: O(1) (checks at most the first 2 characters).
        Space Complexity: O(1)

    Examples:
        >>> start_hi("hi there")
        True
        >>> start_hi("hi")
        True
        >>> start_hi("hello hi")
        False
    """
    return s.startswith("hi")


if __name__ == "__main__":
    print(start_hi("hi there"))
    print(start_hi("hi"))
    print(start_hi("hello hi"))