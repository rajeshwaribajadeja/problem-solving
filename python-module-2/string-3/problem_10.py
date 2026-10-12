"""String-3: sum_numbers problem solution."""


def sum_numbers(s: str) -> int:
    """Return the sum of the numbers appearing in the string.

    Given a string, return the sum of the numbers appearing in the string,
    ignoring all other characters. A number is a series of 1 or more digit
    chars in a row.

    Args:
        s: The input string.

    Returns:
        Sum of all contiguous integer sequences found.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) auxiliary space to collect digit substrings.

    Examples:
        >>> sum_numbers("abc123xyz")
        123
        >>> sum_numbers("aa11b33")
        44
        >>> sum_numbers("7 11")
        18
    """
    total = 0
    number = ""

    for ch in s:
        if ch.isdigit():
            number += ch
        else:
            if number:
                total += int(number)
                number = ""

    if number:
        total += int(number)

    return total


if __name__ == "__main__":
    print(sum_numbers("abc123xyz"))
    print(sum_numbers("aa11b33"))
    print(sum_numbers("7 11"))
