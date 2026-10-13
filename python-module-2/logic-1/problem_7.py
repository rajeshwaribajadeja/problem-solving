"""Logic-1: answer_cell problem solution."""


def answer_cell(is_morning: bool, is_mom: bool, is_asleep: bool) -> bool:
    """Return True if you should answer the cell phone call.

    Normally you answer, except in the morning you only answer if
    it is your mom calling. In all cases, if you are asleep, you
    do not answer.

    Args:
        is_morning: Whether it is morning.
        is_mom: Whether your mom is calling.
        is_asleep: Whether you are asleep.

    Returns:
        True if you should answer the phone, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> answer_cell(False, False, False)
        True
        >>> answer_cell(False, False, True)
        False
        >>> answer_cell(True, False, False)
        False
    """
    return not is_asleep and (not is_morning or is_mom)


if __name__ == "__main__":
    print(answer_cell(False, False, False))
    print(answer_cell(False, False, True))
    print(answer_cell(True, False, False))