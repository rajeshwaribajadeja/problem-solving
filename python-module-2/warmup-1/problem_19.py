"""Warmup-1: endup problem solution."""


def endup(s: str) -> str:
    """Return a string where the last 3 characters are in upper case.

    Given a string, return a new string where the last 3 chars are now
    in upper case. If the string has less than 3 chars, uppercase
    whatever is there.

    Args:
        s: The input string.

    Returns:
        The string with its last 3 characters uppercased.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting string.

    Examples:
        >>> endup("Hello")
        'HeLLO'
        >>> endup("hi there")
        'hi thERE'
        >>> endup("hi")
        'HI'
    """
    return s[:-3] + s[-3:].upper()


if __name__ == "__main__":
    print(endup("Hello"))
    print(endup("hi there"))
    print(endup("hi"))