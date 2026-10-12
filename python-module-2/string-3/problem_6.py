"""String-3: sum_digits problem solution."""


def sum_digits(s: str) -> int:
    """Return the sum of the digits 0-9 that appear in the string.

    Given a string, return the sum of the digits 0-9 that appear in
    the string, ignoring all other characters. Return 0 if there are
    no digits.

    Args:
        s: The input string.

    Returns:
        The sum of all digit characters converted to integers.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> sum_digits("aa1bc2d3")
        6
        >>> sum_digits("aa11b33")
        8
        >>> sum_digits("Chocolate")
        0
    """
    return sum(int(ch) for ch in s if ch.isdigit())


if __name__ == "__main__":
    print(sum_digits("aa1bc2d3"))
    print(sum_digits("aa11b33"))
    print(sum_digits("Chocolate"))