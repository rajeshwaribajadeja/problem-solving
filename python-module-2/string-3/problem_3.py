"""String-3: equal_is_not problem solution."""


def equal_is_not(s: str) -> bool:
    """Return True if appearances of 'is' equals appearances of 'not'.

    Given a string, return True if the number of appearances of "is"
    anywhere in the string is equal to the number of appearances of
    "not" anywhere in the string (case sensitive).

    Args:
        s: The input string.

    Returns:
        True if count of "is" equals count of "not", False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> equal_is_not("This is not")
        False
        >>> equal_is_not("This is notnot")
        True
        >>> equal_is_not("noisxxnotyynotxisi")
        True
    """
    is_count = sum(1 for i in range(len(s) - 1) if s[i:i + 2] == "is")
    not_count = sum(1 for i in range(len(s) - 2) if s[i:i + 3] == "not")
    return is_count == not_count


if __name__ == "__main__":
    print(equal_is_not("This is not"))
    print(equal_is_not("This is notnot"))
    print(equal_is_not("noisxxnotyynotxisi"))
