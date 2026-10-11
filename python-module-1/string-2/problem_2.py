"""String-2: count_hi problem solution."""


def count_hi(s: str) -> int:
    """Return the number of times that the string 'hi' appears in the given string.

    Given a string, return the count of occurrences of the substring "hi".

    Args:
        s: The input string.

    Returns:
        The count of times 'hi' appears in s.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> count_hi('abc hi ho')
        1
        >>> count_hi('ABChi hi')
        2
        >>> count_hi('hihi')
        2
    """
    return s.count("hi")


if __name__ == "__main__":
    print(count_hi("abc hi ho"))
    print(count_hi("ABChi hi"))
    print(count_hi("hihi"))
