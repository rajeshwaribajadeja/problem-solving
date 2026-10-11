"""String-1: non_start problem solution."""


def non_start(a: str, b: str) -> str:
    """Concatenate two strings omitting the first character of each.

    Given 2 strings, return their concatenation, except omit the first
    char of each. The strings will be at least length 1.

    Args:
        a: First string of length 1 or more.
        b: Second string of length 1 or more.

    Returns:
        The concatenated string omitting the first character of each.

    Complexity:
        Time Complexity: O(len(a) + len(b)).
        Space Complexity: O(len(a) + len(b)) to store the sliced concatenated string.

    Examples:
        >>> non_start('Hello', 'There')
        'ellohere'
        >>> non_start('java', 'code')
        'avaode'
        >>> non_start('shotl', 'java')
        'hotlava'
    """
    return a[1:] + b[1:]


if __name__ == "__main__":
    print(non_start("Hello", "There"))
    print(non_start("java", "code"))
    print(non_start("shotl", "java"))