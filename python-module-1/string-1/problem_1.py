"""String-1: hello_name problem solution."""


def hello_name(name: str) -> str:
    """Return a greeting of the form 'Hello <name>!'.

    Given a string name, e.g. "Bob", return a greeting of the form
    "Hello Bob!".

    Args:
        name: The name string.

    Returns:
        A greeting string.

    Complexity:
        Time Complexity: O(N) where N is the length of name.
        Space Complexity: O(N) to store the greeting string.

    Examples:
        >>> hello_name('Bob')
        'Hello Bob!'
        >>> hello_name('Alice')
        'Hello Alice!'
        >>> hello_name('X')
        'Hello X!'
    """
    return f"Hello {name}!"


if __name__ == "__main__":
    print(hello_name("Bob"))
    print(hello_name("Alice"))
    print(hello_name("X"))