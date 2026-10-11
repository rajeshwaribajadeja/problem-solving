"""String-1: ntwice problem solution."""


def ntwice(s: str, n: int) -> str:
    """Return a string made of the first and last n chars from the string.

    Given a string and an int n, return a string made of the first and
    last n chars from the string. The string length will be at least n.

    Args:
        s: An input string of length at least n.
        n: The number of characters to take from start and end.

    Returns:
        A string combining the first n and last n characters.

    Complexity:
        Time Complexity: O(n) (copies 2 * n characters).
        Space Complexity: O(n) to store the result of length 2 * n.

    Examples:
        >>> ntwice("Hello", 2)
        'Helo'
        >>> ntwice("Chocolate", 3)
        'Choate'
        >>> ntwice("Chocolate", 1)
        'Ce'
    """
    return s[:n] + s[-n:]


if __name__ == "__main__":
    print(ntwice("Hello", 2))
    print(ntwice("Chocolate", 3))
    print(ntwice("Chocolate", 1))