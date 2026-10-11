"""String-1: min_cat problem solution."""


def min_cat(a: str, b: str) -> str:
    """Concatenate two strings, trimming the longer one to match lengths.

    Given two strings, append them together (known as "concatenation")
    and return the result. However, if the strings are different lengths,
    omit chars from the longer string so it is the same length as the
    shorter string. The strings may be any length.

    Args:
        a: First string.
        b: Second string.

    Returns:
        The concatenated string with equal-length contributions from each.

    Complexity:
        Time Complexity: O(min(len(a), len(b))).
        Space Complexity: O(min(len(a), len(b))).

    Examples:
        >>> min_cat("Hello", "Hi")
        'loHi'
        >>> min_cat("Hello", "java")
        'ellojava'
        >>> min_cat("java", "Hello")
        'javaello'
    """
    return a[-min(len(a), len(b)):] + b[-min(len(a), len(b)):] if a and b else ""


if __name__ == "__main__":
    print(min_cat("Hello", "Hi"))
    print(min_cat("Hello", "java"))
    print(min_cat("java", "Hello"))
