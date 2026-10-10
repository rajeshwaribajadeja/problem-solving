"""Warmup-1: everynth problem solution."""


def everynth(s: str, n: int) -> str:
    """Return a string starting with char 0 and then every Nth character.

    Given a non-empty string and an int N, return the string made
    starting with char 0, and then every Nth char of the string.

    Args:
        s: The non-empty input string.
        n: The stride step (1 or more).

    Returns:
        The string created by taking every nth character from index 0.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting sliced string.

    Examples:
        >>> everynth("Miracle", 2)
        'Mrce'
        >>> everynth("abcdefg", 2)
        'aceg'
        >>> everynth("abcdefg", 3)
        'adg'
    """
    return s[::n]


if __name__ == "__main__":
    print(everynth("Miracle", 2))
    print(everynth("abcdefg", 2))
    print(everynth("abcdefg", 3))
