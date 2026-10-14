"""Logic-1: fizz_string problem solution."""


def fizz_string(s: str) -> str:
    """Return "Fizz", "Buzz", "FizzBuzz", or the string unchanged.

    If the string starts with "f" return "Fizz".
    If the string ends with "b" return "Buzz".
    If both the "f" and "b" conditions are true, return "FizzBuzz".
    In all other cases, return the string unchanged.

    Args:
        s: The input string.

    Returns:
        "Fizz", "Buzz", "FizzBuzz", or original string s.

    Complexity:
        Time Complexity: O(1)
        Space Complexity: O(1)

    Examples:
        >>> fizz_string("fig")
        'Fizz'
        >>> fizz_string("dib")
        'Buzz'
        >>> fizz_string("fib")
        'FizzBuzz'
    """
    starts_f = s.startswith("f")
    ends_b = s.endswith("b")
    if starts_f and ends_b:
        return "FizzBuzz"
    if starts_f:
        return "Fizz"
    if ends_b:
        return "Buzz"
    return s


if __name__ == "__main__":
    print(fizz_string("fig"))
    print(fizz_string("dib"))
    print(fizz_string("fib"))