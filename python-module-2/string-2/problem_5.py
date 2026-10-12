"""String-2: repeat_front problem solution."""


def repeat_front(s: str, n: int) -> str:
    """Return first n chars, then first n-1 chars, and so on.

    Given a string and an int n, return a string made of the first n
    characters of the string, followed by the first n-1 characters,
    and so on down to 1. Assume 0 <= n <= len(s).

    Args:
        s: The input string.
        n: The initial prefix length (0 <= n <= len(s)).

    Returns:
        The concatenated decreasing prefix string.

    Complexity:
        Time Complexity: O(n^2) to build the string of length n*(n+1)/2.
        Space Complexity: O(n^2) to store the result.

    Examples:
        >>> repeat_front("Chocolate", 4)
        'ChocChoChC'
        >>> repeat_front("Chocolate", 3)
        'ChoChC'
        >>> repeat_front("Ice Cream", 2)
        'IcI'
    """
    return "".join(s[:i] for i in range(n, 0, -1))


if __name__ == "__main__":
    print(repeat_front("Chocolate", 4))
    print(repeat_front("Chocolate", 3))
    print(repeat_front("Ice Cream", 2))
