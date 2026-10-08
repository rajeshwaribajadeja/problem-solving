"""Warmup-1: sleep_in problem solution."""


def sleep_in(weekday: bool, vacation: bool) -> bool:
    """Determine if we can sleep in.

    The parameter weekday is True if it is a weekday, and vacation is True
    if we are on vacation. We sleep in if it is not a weekday or we are on
    vacation.

    Args:
        weekday: True if it is a weekday, False otherwise.
        vacation: True if on vacation, False otherwise.

    Returns:
        True if we can sleep in, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> sleep_in(False, False)
        True
        >>> sleep_in(True, False)
        False
        >>> sleep_in(False, True)
        True
    """
    return not weekday or vacation


if __name__ == "__main__":
    print(sleep_in(False, False))
    print(sleep_in(True, False))
    print(sleep_in(False, True))