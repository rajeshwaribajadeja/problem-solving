"""Array-2: fizz_array problem solution."""


def fizz_array(n: int) -> list:
    """Return an array of length n containing numbers 0, 1, ..., n-1.

    Args:
        n: The desired length of the array.

    Returns:
        A list of integers from 0 to n - 1.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)

    Examples:
        >>> fizz_array(4)
        [0, 1, 2, 3]
        >>> fizz_array(1)
        [0]
        >>> fizz_array(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return list(range(n))


if __name__ == "__main__":
    print(fizz_array(4))
    print(fizz_array(1))
    print(fizz_array(10))
