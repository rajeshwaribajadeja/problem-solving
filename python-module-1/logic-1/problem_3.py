"""Logic-1: squirrel_play problem solution."""


def squirrel_play(temp: int, is_summer: bool) -> bool:
    """Return True if temperature allows squirrels to play.

    Squirrels play if the temperature is between 60 and 90 (inclusive),
    unless it is summer, then the upper limit is 100 instead of 90.

    Args:
        temp: The current temperature.
        is_summer: Whether it is summer.

    Returns:
        True if the squirrels play, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> squirrel_play(70, False)
        True
        >>> squirrel_play(95, False)
        False
        >>> squirrel_play(95, True)
        True
    """
    return 60 <= temp <= 100 if is_summer else 60 <= temp <= 90


if __name__ == "__main__":
    print(squirrel_play(70, False))
    print(squirrel_play(95, False))
    print(squirrel_play(95, True))
