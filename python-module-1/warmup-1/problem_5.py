"""Warmup-1: parrot_trouble problem solution."""


def parrot_trouble(talking: bool, hour: int) -> bool:
    """Determine if we are in trouble due to a talking parrot.

    We have a loud talking parrot. The "hour" parameter is the current hour
    in the range 0..23. We are in trouble if the parrot is talking and the
    hour is before 7 or after 20.

    Args:
        talking: True if the parrot is talking, False otherwise.
        hour: The current hour in the range 0..23.

    Returns:
        True if we are in trouble, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> parrot_trouble(True, 6)
        True
        >>> parrot_trouble(True, 7)
        False
        >>> parrot_trouble(False, 6)
        False
    """
    return talking and (hour < 7 or hour > 20)


if __name__ == "__main__":
    print(parrot_trouble(True, 6))
    print(parrot_trouble(True, 7))
    print(parrot_trouble(False, 6))