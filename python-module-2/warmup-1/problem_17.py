"""Warmup-1: string_e problem solution."""


def string_e(s: str) -> bool:
    """Return True if the given string contains between 1 and 3 'e' characters.

    Return True if the given string contains between 1 and 3 'e' chars.

    Args:
        s: The input string.

    Returns:
        True if the count of 'e' is between 1 and 3 inclusive, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> string_e("Hello")
        True
        >>> string_e("Heelle")
        True
        >>> string_e("Heelele")
        False
    """
    return 1 <= s.count("e") <= 3


if __name__ == "__main__":
    print(string_e("Hello"))
    print(string_e("Heelle"))
    print(string_e("Heelele"))