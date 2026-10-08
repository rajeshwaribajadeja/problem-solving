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


def main() -> None:
    """Run sample test cases for sleep_in."""
    test_cases = [
        (False, False, True),
        (True, False, False),
        (False, True, True),
    ]

    for weekday, vacation, expected in test_cases:
        result = sleep_in(weekday, vacation)
        status = "PASS" if result == expected else "FAIL"
        print(f"sleep_in({weekday}, {vacation}) -> {result} [{status}]")


if __name__ == "__main__":
    main()