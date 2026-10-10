"""Warmup-2: string_bits problem solution."""


def string_bits(s: str) -> str:
    """Return a new string made of every other character starting with the first.

    Given a string, return a new string made of every other char starting
    with the first, so "Hello" yields "Hlo".

    Args:
        s: The input string.

    Returns:
        A string containing every second character starting from index 0.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(N) to store the resulting sliced string.

    Examples:
        >>> string_bits('Hello')
        'Hlo'
        >>> string_bits('Hi')
        'H'
        >>> string_bits('Heeololeo')
        'Hello'
    """
    return s[::2]


if __name__ == "__main__":
    print(string_bits("Hello"))
    print(string_bits("Hi"))
    print(string_bits("Heeololeo"))