"""String-2: mix_string problem solution."""


def mix_string(a: str, b: str) -> str:
    """Interleave characters from two strings with leftovers at the end.

    Given two strings, a and b, create a bigger string made of the first
    char of a, the first char of b, the second char of a, the second char
    of b, and so on. Any leftover chars go at the end of the result.

    Args:
        a: First input string.
        b: Second input string.

    Returns:
        The interleaved string with leftover characters appended.

    Complexity:
        Time Complexity: O(len(a) + len(b)).
        Space Complexity: O(len(a) + len(b)) to store the result.

    Examples:
        >>> mix_string("abc", "xyz")
        'axbycz'
        >>> mix_string("Hi", "There")
        'HTihere'
        >>> mix_string("xxxx", "There")
        'xTxhxexre'
    """
    return "".join(x + y for x, y in zip(a, b)) + a[min(len(a), len(b)):] + b[min(len(a), len(b)):]


if __name__ == "__main__":
    print(mix_string("abc", "xyz"))
    print(mix_string("Hi", "There"))
    print(mix_string("xxxx", "There"))
