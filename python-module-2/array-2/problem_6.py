"""Array-2: fizz_array_2 problem solution."""


def fizz_array_2(n: int) -> list:
    """Return an array of length n containing string forms of 0 to n-1.

    Args:
        n: The desired length of the array.

    Returns:
        A list of string numbers ["0", "1", ..., str(n-1)].

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)

    Examples:
        >>> fizz_array_2(4)
        ['0', '1', '2', '3']
        >>> fizz_array_2(10)
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        >>> fizz_array_2(2)
        ['0', '1']
    """
    return [str(i) for i in range(n)]


if __name__ == "__main__":
    print(fizz_array_2(4))
    print(fizz_array_2(10))
    print(fizz_array_2(2))
