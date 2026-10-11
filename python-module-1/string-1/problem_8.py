"""String-1: without_end problem solution."""


def without_end(s: str) -> str:
    """Return a version of the string without the first and last character.

    Given a string, return a version without the first and last char, so
    "Hello" yields "ell". The string length will be at least 2.

    Args:
        s: An input string of length 2 or more.

    Returns:
        The substring excluding the first and last characters.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the sliced string of length N - 2.

    Examples:
        >>> without_end('Hello')
        'ell'
        >>> without_end('java')
        'av'
        >>> without_end('coding')
        'odin'
    """
    return s[1:-1]


if __name__ == "__main__":
    print(without_end("Hello"))
    print(without_end("java"))
    print(without_end("coding"))
