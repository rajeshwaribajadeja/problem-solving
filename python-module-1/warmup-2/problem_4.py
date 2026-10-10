"""Warmup-2: string_splosion problem solution."""


def string_splosion(s: str) -> str:
    """Return a string made of accumulating prefixes of the original string.

    Given a non-empty string like "Code", return a string like "CCoCodCode".

    Args:
        s: The non-empty input string.

    Returns:
        The concatenated prefix string.

    Complexity:
        Time Complexity: O(N^2) where N is the length of the string.
        Space Complexity: O(N^2) to store the resulting string of length N*(N+1)/2.

    Examples:
        >>> string_splosion('Code')
        'CCoCodCode'
        >>> string_splosion('abc')
        'aababc'
        >>> string_splosion('ab')
        'aab'
    """
    return "".join(s[:i + 1] for i in range(len(s)))


if __name__ == "__main__":
    print(string_splosion("Code"))
    print(string_splosion("abc"))
    print(string_splosion("ab"))