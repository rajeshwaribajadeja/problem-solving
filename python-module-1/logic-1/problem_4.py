"""Logic-1: caught_speeding problem solution."""


def caught_speeding(speed: int, is_birthday: bool) -> int:
    """Return 0 (no ticket), 1 (small ticket), or 2 (big ticket).

    If speed is 60 or less, the result is 0. If speed is between 61 and
    80 inclusive, the result is 1. If speed is 81 or more, the result is 2.
    On your birthday, your speed can be 5 higher in all cases.

    Args:
        speed: The vehicle speed.
        is_birthday: Whether it is the driver's birthday.

    Returns:
        0 for no ticket, 1 for small ticket, or 2 for big ticket.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> caught_speeding(60, False)
        0
        >>> caught_speeding(65, False)
        1
        >>> caught_speeding(65, True)
        0
    """
    return (
        0 if speed <= 60 + (5 if is_birthday else 0)
        else 1 if speed <= 80 + (5 if is_birthday else 0)
        else 2
    )


if __name__ == "__main__":
    print(caught_speeding(60, False))
    print(caught_speeding(65, False))
    print(caught_speeding(65, True))
