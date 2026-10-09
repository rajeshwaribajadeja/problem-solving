"""Warmup-1: front_back problem solution."""


def front_back(s: str) -> str:
    """Exchange the first and last characters of a string.

    Given a string, return a new string where the first and last chars
    have been exchanged.

    Args:
        s: The input string.

    Returns:
        The modified string with first and last characters swapped.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the newly created string.

    Examples:
        >>> front_back('code')
        'eodc'
        >>> front_back('a')
        'a'
        >>> front_back('ab')
        'ba'
    """
    return s if len(s) <= 1 else s[-1] + s[1:-1] + s[0]


if __name__ == "__main__":
    print(front_back("code"))
    print(front_back("a"))
    print(front_back("ab"))
