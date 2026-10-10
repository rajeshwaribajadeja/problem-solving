"""String-2: double_char problem solution."""


def double_char(s: str) -> str:
    """Return a string where for every char in the original, there are two chars.

    Given a string, return a string where for every character in the
    original string, there are two characters.

    Args:
        s: The input string.

    Returns:
        The resulting string with each character doubled.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting doubled string.

    Examples:
        >>> double_char('The')
        'TThhee'
        >>> double_char('AAbb')
        'AAAAbbbb'
        >>> double_char('Hi-There')
        'HHii--TThheerree'
    """
    return "".join(char * 2 for char in s)


if __name__ == "__main__":
    print(double_char("The"))
    print(double_char("AAbb"))
    print(double_char("Hi-There"))
