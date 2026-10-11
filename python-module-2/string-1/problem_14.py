"""String-1: see_color problem solution."""


def see_color(s: str) -> str:
    """Return 'red' or 'blue' if the string starts with either color, else ''.

    Given a string, if the string begins with "red" or "blue" return that
    color string, otherwise return the empty string.

    Args:
        s: The input string.

    Returns:
        "red", "blue", or "" depending on the prefix.

    Complexity:
        Time Complexity: O(1) (checks at most 4 characters).
        Space Complexity: O(1)

    Examples:
        >>> see_color("redxx")
        'red'
        >>> see_color("xxred")
        ''
        >>> see_color("blueTimes")
        'blue'
    """
    return "red" if s.startswith("red") else "blue" if s.startswith("blue") else ""


if __name__ == "__main__":
    print(see_color("redxx"))
    print(see_color("xxred"))
    print(see_color("blueTimes"))