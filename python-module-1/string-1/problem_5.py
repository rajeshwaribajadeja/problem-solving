"""String-1: extra_end problem solution."""


def extra_end(s: str) -> str:
    """Return a new string made of 3 copies of the last 2 chars.

    Given a string, return a new string made of 3 copies of the last 2
    chars of the original string. The string length will be at least 2.

    Args:
        s: The input string of length 2 or more.

    Returns:
        A string consisting of the last 2 characters repeated 3 times.

    Complexity:
        Time Complexity: O(1) (slices at most 2 characters and repeats 3 times).
        Space Complexity: O(1) (resulting string is always length 6).

    Examples:
        >>> extra_end('Hello')
        'lololo'
        >>> extra_end('ab')
        'ababab'
        >>> extra_end('Hi')
        'HiHiHi'
    """
    return s[-2:] * 3


if __name__ == "__main__":
    print(extra_end("Hello"))
    print(extra_end("ab"))
    print(extra_end("Hi"))
