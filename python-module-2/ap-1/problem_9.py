"""AP-1: divides_self problem solution."""


def divides_self(n: int) -> bool:
    """Return True if every digit in the positive integer divides it evenly.

    We'll say that a positive int divides itself if every digit in the
    number divides into the number evenly. 0 does not divide anything
    evenly, so any number containing a 0 digit returns False.

    Args:
        n: A positive integer.

    Returns:
        True if all digits divide n evenly, False otherwise.

    Complexity:
        Time Complexity: O(log10(n)) where n is the given integer.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> divides_self(128)
        True
        >>> divides_self(12)
        True
        >>> divides_self(120)
        False
    """
    temp = n
    while temp > 0:
        digit = temp % 10
        if digit == 0 or n % digit != 0:
            return False
        temp //= 10
    return True


if __name__ == "__main__":
    print(divides_self(128))
    print(divides_self(12))
    print(divides_self(120))