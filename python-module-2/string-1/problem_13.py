"""String-1: last_two problem solution."""


def last_two(s: str) -> str:
    """Return a string where the last 2 characters, if present, are swapped.

    Given a string of any length, return a new string where the last 2
    chars, if present, are swapped, so "coding" yields "codign".

    Args:
        s: The input string.

    Returns:
        The string with the last 2 characters swapped.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the modified string.

    Examples:
        >>> last_two("coding")
        'codign'
        >>> last_two("cat")
        'cta'
        >>> last_two("ab")
        'ba'
    """
    return s[:-2] + s[-1] + s[-2] if len(s) >= 2 else s


if __name__ == "__main__":
    print(last_two("coding"))
    print(last_two("cat"))
    print(last_two("ab"))