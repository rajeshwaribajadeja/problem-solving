"""String-1: combo_string problem solution."""


def combo_string(a: str, b: str) -> str:
    """Return a string in the form short + long + short.

    Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the
    inside. The strings will not be the same length, but they may be empty.

    Args:
        a: First string.
        b: Second string.

    Returns:
        The concatenated string in the pattern short + long + short.

    Complexity:
        Time Complexity: O(len(a) + len(b)).
        Space Complexity: O(len(a) + len(b)) to store the composite string.

    Examples:
        >>> combo_string('Hello', 'hi')
        'hiHellohi'
        >>> combo_string('hi', 'Hello')
        'hiHellohi'
        >>> combo_string('aaa', 'b')
        'baaab'
    """
    return a + b + a if len(a) < len(b) else b + a + b


if __name__ == "__main__":
    print(combo_string("Hello", "hi"))
    print(combo_string("hi", "Hello"))
    print(combo_string("aaa", "b"))