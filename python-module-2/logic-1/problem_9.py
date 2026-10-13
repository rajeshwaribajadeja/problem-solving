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
    return "FizzBuzz" if s.startswith("f") and s.endswith("b") else "Fizz" if s.startswith("f") else "Buzz" if s.endswith("b") else s


if __name__ == "__main__":
    print(fizz_string("fig"))
    print(fizz_string("dib"))
    print(fizz_string("fib"))