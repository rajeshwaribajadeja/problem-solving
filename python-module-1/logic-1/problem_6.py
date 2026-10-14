"""Logic-1: alarm_clock problem solution."""


def alarm_clock(day: int, vacation: bool) -> str:
    """Return the time the alarm clock should ring.

    Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
    and a boolean vacation flag, return when the alarm clock should ring.
    Weekdays: "7:00", weekends: "10:00". On vacation: weekdays "10:00",
    weekends "off".

    Args:
        day: Day of the week (0=Sun, 1=Mon, ..., 6=Sat).
        vacation: Whether we are on vacation.

    Returns:
        The alarm time string ("7:00", "10:00", or "off").

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> alarm_clock(1, False)
        '7:00'
        >>> alarm_clock(5, False)
        '7:00'
        >>> alarm_clock(0, False)
        '10:00'
    """
    is_weekend = day in (0, 6)
    return (
        "off" if vacation and is_weekend
        else "10:00" if vacation or is_weekend
        else "7:00"
    )


if __name__ == "__main__":
    print(alarm_clock(1, False))
    print(alarm_clock(5, False))
    print(alarm_clock(0, False))