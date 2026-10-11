"""String-1: front_again problem solution."""


def front_again(s: str) -> bool:
    """Return True if the first 2 characters also appear at the end.

    Given a string, return True if the first 2 chars in the string also
    appear at the end of the string, such as with "edited".

    Args:
        s: The input string.

    Returns:
        True if first 2 characters equal last 2 characters, False otherwise.

    Complexity:
        Time Complexity: O(1) (checks at most 2 characters at ends).
        Space Complexity: O(1)

    Examples:
        >>> front_again("edited")
        True
        >>> front_again("edit")
        False
        >>> front_again("ed")
        True
    """
    return len(s) >= 2 and s[:2] == s[-2:]


if __name__ == "__main__":
    print(front_again("edited"))
    print(front_again("edit"))
    print(front_again("ed"))