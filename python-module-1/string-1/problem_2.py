"""String-1: make_abba problem solution."""


def make_abba(a: str, b: str) -> str:
    """Return strings combined in the order a + b + b + a.

    Given two strings, a and b, return the result of putting them
    together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

    Args:
        a: First string.
        b: Second string.

    Returns:
        The concatenated abba string.

    Complexity:
        Time Complexity: O(len(a) + len(b)).
        Space Complexity: O(len(a) + len(b)) to store the combined string.

    Examples:
        >>> make_abba('Hi', 'Bye')
        'HiByeByeHi'
        >>> make_abba('Yo', 'Alice')
        'YoAliceAliceYo'
        >>> make_abba('What', 'Up')
        'WhatUpUpWhat'
    """
    return a + b + b + a


if __name__ == "__main__":
    print(make_abba("Hi", "Bye"))
    print(make_abba("Yo", "Alice"))
    print(make_abba("What", "Up"))