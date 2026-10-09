"""Warmup-1: monkey_trouble problem solution."""


def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    """Determine if we are in trouble with the monkeys.

    We have two monkeys, a and b, and the parameters a_smile and b_smile
    indicate if each is smiling. We are in trouble if they are both
    smiling or if neither of them is smiling.

    Args:
        a_smile: True if monkey a is smiling, False otherwise.
        b_smile: True if monkey b is smiling, False otherwise.

    Returns:
        True if we are in trouble, False otherwise.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> monkey_trouble(True, True)
        True
        >>> monkey_trouble(False, False)
        True
        >>> monkey_trouble(True, False)
        False
    """
    return a_smile == b_smile


if __name__ == "__main__":
    print(monkey_trouble(True, True))
    print(monkey_trouble(False, False))
    print(monkey_trouble(True, False))